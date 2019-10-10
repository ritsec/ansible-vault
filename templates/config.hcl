storage "file" {
    path = "/mnt/vault/data"  # TODO: fix
}

listener "tcp" {
    address = "0.0.0.0:8200"
}

cluster_name = "name"  # TODO: fix
ui = true