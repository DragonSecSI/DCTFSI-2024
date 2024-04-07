data "azurerm_resource_group" "challs" {
  name     = var.azure_resource_group_name
}

data "azurerm_kubernetes_cluster" "k8s" {
  name                = var.azure_k8s_cluster_name
  resource_group_name = data.azurerm_resource_group.challs.name
}

resource "azurerm_public_ip" "challs_pwn" {
  name                = "challs_pwn_public_ip"
  resource_group_name = "MC_${data.azurerm_resource_group.challs.name}_${data.azurerm_kubernetes_cluster.k8s.name}_${data.azurerm_resource_group.challs.location}"
  location            = data.azurerm_resource_group.challs.location
  allocation_method   = "Static"
  sku                 = "Standard"
}

module "nginx-controller" {
  source  = "terraform-iaac/nginx-controller/helm"
  version = "2.0.1"
}
