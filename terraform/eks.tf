provider "aws" {
  region = "us-west-2"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "message-api-cluster"
  cluster_version = "1.21"
  subnets         = ["subnet-0bb1c79de3EXAMPLE", "subnet-0bb1c79de4EXAMPLE"]

  node_groups = {
    eks_nodes = {
      desired_capacity = 2
      max_capacity     = 5
      min_capacity     = 1

      instance_type = "t3.medium"
    }
  }
}
