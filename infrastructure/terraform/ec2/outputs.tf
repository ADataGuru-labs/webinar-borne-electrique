output "ec2_public_ip" {
  description = "The ip of the machine"
  value       = aws_instance.nomalisation_borne_electrique.public_ip
}

output "ec2_public_dns" {
  description = "The ip of the machine"
  value       = aws_instance.nomalisation_borne_electrique.public_dns
}

output "ssh_connect_cli" {
  description = "The command to enter for ssh connect to the machine"
  value       = "ssh -i ${var.aws_private_key_ssh_path} ubuntu@${aws_instance.nomalisation_borne_electrique.public_dns}"
}