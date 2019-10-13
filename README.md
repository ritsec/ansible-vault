vault
=========

An Ansible role to deploy and configure HashiCorp Vault.

Requirements
------------

This role does not have any additional requirements.

Role Variables
--------------

### General Variables

#### `vault_user_name`: vault
- Name of system user to add that Vault will run as.

#### `vault_user_gecos`: HashiCorp Vault
- Comment/GECOS string of the Vault user.

#### `vault_installation_path`: /opt/vault
- Folder to place the Vault binary and configuration file.

#### `vault_download_fullurl`: "{{ vault_download_url }}/{{ vault_version }}/vault_{{ vault_version }}_linux_amd64.zip"
- Full URL that Vault will be downloaded from.
- Override this variable if you would like to download the Vault zipfile from a
  custom source.

#### `vault_version`: 1.2.3
- Version of Vault to install.
- Used to construct `vault_download_fullurl`.
- Used in the systemd service file.

#### `vault_download_baseurl`: https://releases.hashicorp.com/vault/
- Website and path to download Vault from.
- Only used to construct `vault_download_fullurl`.

#### `vault_symlink_target`: "/usr/local/bin/vault"
- Where to create a symbolic link to the Vault binary. Should be in the $PATH.

#### `vault_servicefile_path`: "/etc/systemd/system/vault.service"
- Where to place the Vault systemd service file.

### Vault Configuration File (General)

These variables are used to generate the Vault configuration file. Check out
[the Vault documentation](https://www.vaultproject.io/docs/configuration/index.html)
for more information.

#### `vault_cluster_name`:
- The name of the Vault cluster. By default this is unset, and Vault will
  automatically generate a cluster name. Set this variable if you want a custom
  cluster name.

#### `vault_ui`: "false"
- Whether the HTTP UI should be enabled.

#### `vault_ha`: false
- Whether to set up high availability for Vault. Should only be true if using
  Consul as the storage backend.

#### `vault_api_addr`: ""
- The address that will be advertised to other Vault servers in the cluster for
  client redirection. Only used when `vault_ha` is set to true.

#### `vault_cluster_addr`: ""
- The address that will be advertised to other Vault servers in the cluster for
  request forwarding. Only used when `vault_ha` is set to true.

#### `vault_disable_clustering`: "false"
- Whether cluster features like request forwarding are enabled. Only used when
  `vault_ha` is set to true.

### Vault Configuration File (Listener)

These variables are used to configure the TCP listener in the Vault
configuration file. Only one listener is currently supported. Check out
[the Vault documentation](https://www.vaultproject.io/docs/configuration/listener/tcp.html)
for more information.

#### `vault_tcp_address`: "127.0.0.1:8200"
- The address to listen on for client connections.

#### `vault_tcp_cluster_address`: "127.0.0.1:8201"
- The address to listen on for connections from servers in the cluster.

#### `vault_tcp_tls_disable`: "false"
- Whether to listen on HTTPS for all connections.

#### `vault_tcp_tls_cert_file`: ""
- The path to the certificate that will be used for HTTPS.

#### `vault_tcp_tls_key_file`: ""
- The path to the private key that will be used for HTTPS.

### Vault Configuration File (Storage Backend)

These variables are used to configure the storage backend. The only backends
that are currently supported are Consul, Filesystem, and In-Memory. Check out
[the Vault documentation](https://www.vaultproject.io/docs/configuration/storage/index.html)
for more information on each storage backend.

#### `vault_storage_backend`: file
- Which storage backend to use.
- The following values are supported:
  - "consul": uses the Consul backend
  - "file": uses the Filesystem backend
  - "inmem": uses the In-Memory backend

#### `vault_filesystem_path:` ""
- The path on the filesystem to which Vault will store data.
- A new directory named `vault/` will be created under this path.
- Only used when `vault_storage_backend` is set to "file".

#### `vault_consul_address`: "127.0.0.1:8500"
- The address of the Consul agent to communicate with.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_disable_registration`: "false"
- Whether Vault should register itself with Consul.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_path`: "vault/"
- The path in Consul's key-vaul store where Vault data will be stored.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_scheme`: "http"
- The scheme to use when communicating with Consul. Supported values are "http"
  and "https".
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_service`: "vault"
- The name of the service to register in Consul.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_service_tags`: ""
- A comma-separated list of tags to attach to the service registration in
  Consul.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_token`: ""
- A Consul ACL token with read/write permissions to the path specified in
  `vault_consul_path`.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_tls_ca_file`: ""
- The CA certificate used for Consul communication. Only used when the Consul
  scheme is https.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_tls_cert_file`: ""
- The certificate used for Consul communication. Only used when the Consul
  scheme is https.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_tls_key_file`: ""
- The private key used for Consul communication. Only used when the Consul
  scheme is https.
- Only used when `vault_storage_backend` is set to "consul".

#### `vault_consul_tls_min_version:` "tls12"
- The minimum TLS version to be used for Consul communication. Only used when
  the Consul scheme is https.
- Only used when `vault_storage_backend` is set to "consul".

Dependencies
------------

This role does not depend on any other roles.

Example Playbook
----------------

```yaml
- hosts: all
  become: true
  vars:
    vault_ui: "true"
    vault_tcp_address: "0.0.0.0:8200"
    vault_tcp_tls_disable: "true"
    vault_filesystem_path: "/tmp"
  roles:
    - vault
```

License
-------

BSD

Author Information
------------------

Author: RITSEC Operations Program
