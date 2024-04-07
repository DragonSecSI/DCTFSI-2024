terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.98.0"
    }
    cloudflare = {
      source = "cloudflare/cloudflare"
      version = "~> 4.29.0"
    }
    acme = {
      source  = "vancluever/acme"
      version = "~> 2.21.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "DCTFSI24"
    storage_account_name = "dctf24"
    container_name       = "tfstate"
    key                  = "dctf"
  }
}

provider "azurerm" {
  features {}
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

provider "acme" {
  server_url = "https://acme-v02.api.letsencrypt.org/directory"
}

provider "kubernetes" {
  host                   = "${data.azurerm_kubernetes_cluster.k8s.kube_config.0.host}"
  username               = "${data.azurerm_kubernetes_cluster.k8s.kube_config.0.username}"
  password               = "${data.azurerm_kubernetes_cluster.k8s.kube_config.0.password}"
  client_certificate     = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.client_certificate)}"
  client_key             = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.client_key)}"
  cluster_ca_certificate = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.cluster_ca_certificate)}"
}

provider "helm" {
  kubernetes {
    host                   = "${data.azurerm_kubernetes_cluster.k8s.kube_config.0.host}"
    client_certificate     = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.client_certificate)}"
    client_key             = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.client_key)}"
    cluster_ca_certificate = "${base64decode(data.azurerm_kubernetes_cluster.k8s.kube_config.0.cluster_ca_certificate)}"
  }
}
