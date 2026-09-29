
output "aws_eks_ip" {
  value = aws_instance.aws-eks.public_ip
}

