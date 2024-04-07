resource "kubernetes_secret" "dctf-wildcard" {
  metadata {
    name = "dctf-wildcard"
  }

  data = {
    "tls.crt" = module.acme_dctf_wildcard_certificate.certificate
    "tls.key" = module.acme_dctf_wildcard_certificate.private_key
  }

  type = "kubernetes.io/tls"
}

resource "kubernetes_secret" "registry_secret" {
  metadata {
    name = "registry-secret"
    namespace = var.azure_k8s_namespace
  }

  type = "kubernetes.io/dockerconfigjson"
  data = {
    ".dockerconfigjson" = jsonencode({
      auths = {
        "${var.azure_k8s_registry_host}" = {
          "username" = var.azure_k8s_registry_user
          "password" = var.azure_k8s_registry_password
          "auth"     = base64encode("${var.azure_k8s_registry_user}:${var.azure_k8s_registry_password}")
        }
      }
    })
  }
}
