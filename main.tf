data "aws_caller_identity" "default" {}
data "aws_region" "default" {}

resource "aws_sns_topic" "main" {
  name = "${var.project}-${var.environment}-notifications-formatter"
}

locals {
  notifications_formatter_lambda_name         = "${var.project}-${var.environment}-notification-formatter"
  notifications_formatter_lambda_zip_filename = "${path.module}/formatter.zip"
}

data "archive_file" "notifications_formatter" {
  type             = "zip"
  source_dir      = "${path.module}/lambda"
  output_path      = local.notifications_formatter_lambda_zip_filename
  output_file_mode = "0755"
}

resource "aws_lambda_function" "notifications_formatter" {
  function_name    = local.notifications_formatter_lambda_name
  role             = aws_iam_role.notifications_formatter.arn
  filename         = local.notifications_formatter_lambda_zip_filename
  handler          = "main.lambda_handler"
  runtime          = "python3.13"
  timeout          = 3
  memory_size      = 128
  source_code_hash = data.archive_file.notifications_formatter.output_base64sha256

  environment {
    variables = {
      FORMATTERS = join(",", coalesce(var.formatters, ["ignore_create_service_linked_role", "cloud_watch_alarm", "iam_changes"]))
    }
  }

  depends_on = [
    aws_iam_role.notifications_formatter,
    aws_cloudwatch_log_group.notifications_formatter
  ]

}

resource "aws_cloudwatch_log_group" "notifications_formatter" {
  name              = "/aws/lambda/${local.notifications_formatter_lambda_name}"
  retention_in_days = var.log_retention
}


################################################
#### IAM                                    ####
################################################

resource "aws_iam_role" "notifications_formatter" {
  name               = "${local.notifications_formatter_lambda_name}-${data.aws_region.default.id}"
  description        = "Role used for lambda function ${local.notifications_formatter_lambda_name}"
  assume_role_policy = data.aws_iam_policy_document.assume_role_notification.json
}

resource "aws_iam_role_policy" "notifications_formatter" {
  name   = "${local.notifications_formatter_lambda_name}-policy"
  policy = data.aws_iam_policy_document.role_notification.json
  role   = aws_iam_role.notifications_formatter.id
}

data "aws_iam_policy_document" "assume_role_notification" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "role_notification" {
  statement {
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = [
      "${aws_cloudwatch_log_group.notifications_formatter.arn}*"
    ]
  }
}
