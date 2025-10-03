variable "environment" {
  description = "Environment name"
}

variable "project" {
  description = "Project name"
}

variable "log_retention" {
  type        = number
  default     = 7
  description = "How long to keep logs"
}

variable "formatters" {
    type        = list(string)
    description = "List of formatters"
    default     = null
}