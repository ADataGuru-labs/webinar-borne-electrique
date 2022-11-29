terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.41.0"
    }
  }
}
# PROVIDER
provider "aws" {
  region = var.region
}