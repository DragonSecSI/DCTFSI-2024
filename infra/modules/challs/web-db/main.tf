resource "kubernetes_ingress_v1" "ingress" {
  metadata {
    name = "web-${var.name}-ingress"
    namespace = var.k8s_namespace

    annotations = {
      "kubernetes.io/ingress.class" = "nginx"
    }
  }

  spec {
    rule {
      host = "${var.hostname}"
      http {
        path {
          backend {
            service {
              name = kubernetes_service_v1.service.metadata.0.name
              port {
                number = 3000
              }
            }
          }

          path = "/"
        }
      }
    }

    tls {
      secret_name = var.tls
    }
  }

  wait_for_load_balancer = true
}

resource "kubernetes_service_v1" "service" {
  metadata {
    name = "web-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment_v1.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 3000
      target_port = 3000
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment_v1" "deployment" {
  metadata {
    name = "web-${var.name}-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "${var.name}"
      }
    }

    template {
      metadata {
        labels = {
          app = "${var.name}"
        }
      }

      spec {
        node_selector = {
          agentpool = "challs"
        }
        container {
          image = "${var.k8s_image}"
          name  = "${var.name}"

          security_context {
            run_as_user                = 1337
            run_as_group               = 1337
            run_as_non_root            = true
            read_only_root_filesystem  = true
            privileged                 = false
            allow_privilege_escalation = false
            capabilities {
              add = [
                "NET_BIND_SERVICE",
              ]
            }
          }
          
          env {
            name  = "MYSQL_HOST"
            value = kubernetes_service_v1.db_service.metadata.0.name
          }
          env {
            name  = "MYSQL_DATABASE"
            value = "musixdb"
          }
          env {
            name  = "MYSQL_USER"
            value = "musix"
          }
          env {
            name  = "MYSQL_ROOT_PASSWORD"
            value = "Massager-Trailing-Playing4-Outpost-Delicate-Wieldable"
          }
          env {
            name  = "MYSQL_PASSWORD"
            value = "Partly-Habitual-Pulp2-Dry-Bobtail-Operate"
          }

          resources {
            limits = {
              cpu    = "0.3"
              memory = "256Mi"
            }
            requests = {
              cpu    = "0.1"
              memory = "256Mi"
            }
          }
        }

        image_pull_secrets {
          name = var.k8s_registry_secret
        }
      }
    }
  }
}
