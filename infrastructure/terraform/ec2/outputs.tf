output "ec2_public_ip" {
  description = "The ip of the machine"
  value       = aws_instance.nomalisation_borne_electrique.public_ip
}

output "ec2_public_dns" {
  description = "The ip of the machine"
  value       = aws_instance.nomalisation_borne_electrique.public_dns
}