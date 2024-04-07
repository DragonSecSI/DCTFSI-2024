module "acme_dctf_wildcard_certificate" {
  source = "./modules/acme"

  registration_email = var.certificate_registration_email
  common_name        = "*.dctf.si"

  cloudflare_api_token = var.cloudflare_api_token
}
