terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.25"
    }
  }

  backend "s3" {
    bucket = "daaas-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

# EKS Cluster
module "eks" {
  source = "./modules/eks"

  cluster_name    = var.cluster_name
  cluster_version = "1.28"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets
}

# VPC
module "vpc" {
  source = "./modules/vpc"

  name       = "${var.project_name}-vpc"
  cidr_block = var.vpc_cidr
}

# RDS PostgreSQL
module "rds" {
  source = "./modules/rds"

  identifier     = "${var.project_name}-db"
  engine_version = "16.1"
  instance_class = var.db_instance_class
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.private_subnets
}

# ElastiCache Redis
module "redis" {
  source = "./modules/redis"

  cluster_id     = "${var.project_name}-redis"
  node_type      = var.redis_node_type
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.private_subnets
}

# S3 Bucket for file storage
resource "aws_s3_bucket" "uploads" {
  bucket = "${var.project_name}-uploads-${var.environment}"
  tags = {
    Project     = var.project_name
    Environment = var.environment
  }
}
