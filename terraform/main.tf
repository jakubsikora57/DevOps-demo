terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "DevOps-demo" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = "DevOps-demo"
  }
}
