#module "chall_crypto_padding_oracle" {
#  source = "./modules/challs/pwn/"
#  count = 1
#
#  name = "paddingoracle"
#  ip   = azurerm_public_ip.challs_pwn.ip_address
#  port = 13370
#
#  k8s_namespace       = "default"
#  k8s_image           = "dctf24.azurecr.io/challs/paddingoracle:latest"
#  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
#}
#
#module "chall_pwn_admin_login" {
#  source = "./modules/challs/pwn/"
#  count = 1
#
#  name = "adminlogin"
#  ip   = azurerm_public_ip.challs_pwn.ip_address
#  port = 13371
#
#  k8s_namespace       = "default"
#  k8s_image           = "dctf24.azurecr.io/challs/adminlogin:latest"
#  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
#}
#
#module "chall_pwn_librarians_revenge" {
#  source = "./modules/challs/pwn/"
#  count = 1
#
#  name = "librariansrevenge"
#  ip   = azurerm_public_ip.challs_pwn.ip_address
#  port = 13372
#
#  k8s_namespace       = "default"
#  k8s_image           = "dctf24.azurecr.io/challs/librariansrevenge:latest"
#  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
#}
#
#module "chall_pwn_gambler" {
#  source = "./modules/challs/pwn/"
#  count = 1
#
#  name = "gambler"
#  ip   = azurerm_public_ip.challs_pwn.ip_address
#  port = 13373
#
#  k8s_namespace       = "default"
#  k8s_image           = "dctf24.azurecr.io/challs/gambler:latest"
#  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
#}
#
#module "chall_pwn_integer" {
#  source = "./modules/challs/pwn/"
#  count = 1
#
#  name = "integer"
#  ip   = azurerm_public_ip.challs_pwn.ip_address
#  port = 13374
#
#  k8s_namespace       = "default"
#  k8s_image           = "dctf24.azurecr.io/challs/integer:latest"
#  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name
#}
