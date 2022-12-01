resource "aws_key_pair" "admin" {
  key_name   = "admin"
  public_key = file(var.aws_public_key_ssh_path)
}

resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_default_security_group" "ssh_open" {
  vpc_id = aws_default_vpc.default.id
  ingress {
    # TLS (change to whatever ports you need)
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    # Please restrict your ingress to only necessary IPs and ports.
    # Opening to 0.0.0.0/0 can lead to security vulnerabilities.
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    # TLS (change to whatever ports you need)
    from_port = 5000
    to_port   = 5000
    protocol  = "tcp"
    # Please restrict your ingress to only necessary IPs and ports.
    # Opening to 0.0.0.0/0 can lead to security vulnerabilities.
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "nomalisation_borne_electrique" {
  ami                  = var.ami_id
  instance_type        = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.normalisation_borne_electrique.name

  key_name = aws_key_pair.admin.key_name

  tags = {
    Name = var.tag_name
  }

}