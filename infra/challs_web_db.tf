module "chall_webdb_musix" {
  source = "./modules/challs/web-db/"
  count = 1

  name     = "musix"
  hostname = "musix.dctf.si"
  tls      = kubernetes_secret.dctf-wildcard.metadata.0.name

  k8s_namespace       = "default"
  k8s_image           = "dctf24.azurecr.io/challs/musix:latest"
  k8s_registry_secret = kubernetes_secret.registry_secret.metadata.0.name

  cloudflare_name    = "musix"
  cloudflare_zone_id = data.cloudflare_zone.dctf.id
  cloudflare_proxied = false
  cloudflare_ttl     = 1
}
