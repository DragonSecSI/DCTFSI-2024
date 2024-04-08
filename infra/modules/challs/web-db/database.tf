resource "kubernetes_service_v1" "db_service" {
  metadata {
    name = "web-${var.name}-db-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment_v1.db_deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 3306
      target_port = 3306
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment_v1" "db_deployment" {
  metadata {
    name = "web-${var.name}-db-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "${var.name}-db"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "${var.name}-db"
      }
    }

    template {
      metadata {
        labels = {
          app = "${var.name}-db"
        }
      }

      spec {
        node_selector = {
          agentpool = "challs"
        }
        container {
          image = "mysql:5.7"
          name  = "${var.name}-db"

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

          volume_mount {
            name       = "db-config"
            mount_path = "/docker-entrypoint-initdb.d/00-init.sql"
            sub_path   = "00-init.sql"
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

        volume {
          name = "db-config"
          config_map {
            name = kubernetes_config_map.db_config_map.metadata.0.name
            items {
              key  = "00-init.sql"
              path = "00-init.sql"
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

resource "kubernetes_config_map" "db_config_map" {
  metadata {
    name = "web-${var.name}-db-config"
    namespace = var.k8s_namespace
  }

  data = {
    "00-init.sql" = file("${path.module}/files/00-init.sql")
  }
}
