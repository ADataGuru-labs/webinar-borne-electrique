variable "region" {
  description = "The aws region the resources will be build"
  type        = string
  default = "eu-west-1"
}

variable "instance_type" {
  description = "aws ec2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "tag_name" {
  description = "Aws tag name permit to search an instance by tag"
  type        = string
  default     = "instance-borne-electrique"
}