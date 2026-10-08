
resource "aws_instance" "aws-eks" {
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = "abi"
  subnet_id                   = aws_subnet.myapp-subnet-3.id
  vpc_security_group_ids      = [aws_default_security_group.default-sg.id]
  availability_zone           = var.avail_zone3
  associate_public_ip_address = true
  tags = {
    Name = "${var.env_prefix}-aws-eks"
  }
}