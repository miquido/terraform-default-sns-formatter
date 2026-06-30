# default-sns-formatter <a href="https://miquido.com"><img align="right" src="https://cdn.miquido.dev/miquido-logo.png" width="150" /></a>

Terraform module that provisions an AWS Lambda function for formatting and routing SNS notifications

## Development

```bash
make init   # run once after cloning
make readme # regenerate README.md
make lint   # lint terraform code
```

## Usage

```hcl
module "sns_formatter" {
  source = "git@gitlab.miquido.com:miquido/terraform/default-sns-formatter.git"

  project     = "my-project"
  environment = "production"
}
```

<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
| ---- | ------- |
| <a name="provider_archive"></a> [archive](#provider\_archive) | 2.8.0 |
| <a name="provider_aws"></a> [aws](#provider\_aws) | 6.52.0 |

## Modules

No modules.

## Resources

| Name | Type |
| ---- | ---- |
| [aws_cloudwatch_log_group.notifications_formatter](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_iam_role.notifications_formatter](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy.notifications_formatter](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy) | resource |
| [aws_lambda_function.notifications_formatter](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |

## Inputs

| Name | Description | Type | Default | Required |
| ---- | ----------- | ---- | ------- | :------: |
| <a name="input_environment"></a> [environment](#input\_environment) | Environment name | `any` | n/a | yes |
| <a name="input_filename"></a> [filename](#input\_filename) | Custom python code filename for formatter | `string` | `null` | no |
| <a name="input_formatters"></a> [formatters](#input\_formatters) | List of formatters | `list(string)` | `null` | no |
| <a name="input_handler"></a> [handler](#input\_handler) | Custom python code handler for formatter | `string` | `null` | no |
| <a name="input_log_retention"></a> [log\_retention](#input\_log\_retention) | How long to keep logs | `number` | `7` | no |
| <a name="input_name"></a> [name](#input\_name) | Custom name | `string` | `"default"` | no |
| <a name="input_project"></a> [project](#input\_project) | Project name | `any` | n/a | yes |
| <a name="input_source_code_hash"></a> [source\_code\_hash](#input\_source\_code\_hash) | Custom python code hash for formatter | `string` | `null` | no |

## Outputs

| Name | Description |
| ---- | ----------- |
| <a name="output_formatter_lambda_arn"></a> [formatter\_lambda\_arn](#output\_formatter\_lambda\_arn) | ARN of the SNS formatter Lambda function |
<!-- END_TF_DOCS -->

## License

[MIT](LICENSE)
