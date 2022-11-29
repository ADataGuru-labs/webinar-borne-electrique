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

variable "ami_id" {
  description = "id of an ami by default it's ubuntu 18.04"
  type        = string
}

variable "aws_public_key_ssh_path" {
  description = "The key name of the Key Pair to use for the instance"
  type        = string
}

variable "aws_private_key_ssh_path" {
  description = "The key name of the Key Pair to use for the instance"
  type        = string
}