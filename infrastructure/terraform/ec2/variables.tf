variable "region" {
  description = "The aws region the resources will be build"
  type        = string
}

variable "ami_id" {
  description = "id of an ami by default it's ubuntu 18.04"
  type        = string
  default     = "ami-03ef731cc103c9f09"
}

variable "instance_type" {
  description = "aws ec2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "tag_name" {
  description = "Aws tag name permit to search an instance by tag"
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