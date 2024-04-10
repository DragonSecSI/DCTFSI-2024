module "chall_web_pack_the_flag" {
  source = "./modules/challs/web"
  count = 1

  name     = "packtheflag"
  hostname = "packtheflag.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/packtheflag:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "packtheflag"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  port = 8000
}

module "chall_web_back_me_up" {
  source = "./modules/challs/web-back-me-up"
  count = 1

  name     = "backmeup"
  hostname = "backmeup.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/backmeup:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "backmeup"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  port = 8000
}

module "chall_web_i7n" {
  source = "./modules/challs/web"
  count = 1

  name     = "i7n"
  hostname = "i7n.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/i7n:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "i7n"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1

  port = 80
}
