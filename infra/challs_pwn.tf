module "chall_crypto_padding_oracle" {
  source = "./modules/challs/pwn/"
  count = 1

  name = "paddingoracle"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13370

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/paddingoracle:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_library_shelves" {
  source = "./modules/challs/pwn/"
  count = 1

  name = "libraryshelves"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13371

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/libraryshelves:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}

module "chall_pwn_librarians_revenge" {
  source = "./modules/challs/pwn/"
  count = 1

  name = "librariansrevenge"
  ip   = azurerm_public_ip.challs_pwn.ip_address
  port = 13372

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/librariansrevenge:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
}
