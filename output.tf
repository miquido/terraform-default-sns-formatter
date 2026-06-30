output "formatter_lambda_arn" {
  description = "ARN of the SNS formatter Lambda function"
  value       = aws_lambda_function.notifications_formatter.arn
}