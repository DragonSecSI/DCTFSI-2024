# Cloudflare

variable "cloudflare_api_token" {
  description = "Cloudflare API token"
  type        = string
  sensitive   = true
  nullable    = false
}

# Config

variable "azure_resource_group_name" {}
variable "azure_resource_group_location" {}

variable "azure_k8s_cluster_name" {}

variable "azure_k8s_registry_host" {}
variable "azure_k8s_registry_user" {}
variable "azure_k8s_registry_password" {}
variable "azure_k8s_namespace" {}

variable "certificate_registration_email" {}
