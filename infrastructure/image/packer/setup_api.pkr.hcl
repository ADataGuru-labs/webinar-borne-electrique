variable "region" {
  type =  string
  default = "eu-west-1"
}

variable "user" {
  type = string
  default = "ubuntu"
}

data "amazon-ami" "ubuntu_image" {
  filters = {
    virtualization-type = "hvm"
    name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
    root-device-type    = "ebs"
  }
  owners      = ["099720109477"]
  most_recent = true
  region      = var.region
}


source "amazon-ebs" "ubuntu" {
  ami_name             = "packer_AWS {{timestamp}}"
  instance_type        = "t2.micro"
  region               = var.region
  source_ami           = data.amazon-ami.ubuntu_image.id
  ssh_username         = var.user
  communicator         = "ssh"
  temporary_iam_instance_profile_policy_document {
    Statement {
        Action   = ["logs:*"]
        Effect   = "Allow"
        Resource = ["*"]
    }
    Version = "2012-10-17"
}
}

build {
  sources = [
    "amazon-ebs.ubuntu"
  ]
   provisioner "ansible" {
      playbook_file = "infrastructure/ansible/setup_api.yml"
      ansible_env_vars =  [
        "ANSIBLE_HOST_KEY_CHECKING=False"
      ]
      user= var.user
    }
}
