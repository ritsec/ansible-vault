storage "file" {
    path = "/mnt/vault/data"  # TODO: fix
}

listener "tcp" {
    address = "0.0.0.0:8200"
    tls_cert_file = "/opt/vault/vault-cert.pem"
    tls_key_file = "/opt/vault/vault-key.pem"
}

cluster_name = "name"  # TODO: fix
ui = true