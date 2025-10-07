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

variable "filename" {
  type = string
  description = "Custom python code filename for formatter"
  default = null
}

variable "source_code_hash" {
  type = string
  description = "Custom python code hash for formatter"
  default = null
}

variable "handler" {
  type = string
  description = "Custom python code handler for formatter"
  default = null
}
