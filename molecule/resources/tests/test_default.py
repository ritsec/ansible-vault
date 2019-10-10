import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

FILES = [
    "/usr/local/bin/vault",
    "/opt/vault/vault",
    "/opt/vault/config.hcl",
    "/opt/vault/vault-key.pem",
    "/opt/vault/vault-cert.pem",
]


def test_user(host):
    user = host.user("vault")

    assert user.exists
    assert user.gecos == "HashiCorp Vault"
    # Not fantastic test to make sure it's a system account instead of a user account
    assert user.uid < 1000
    assert user.gid < 1000
    assert user.group == "vault"


def test_files(host):
    # Test for vault directory
    assert host.file("/opt/vault").exists
    assert host.file("/opt/vault").is_directory

    # Test for various vault directories
    for file_path in FILES:
        assert host.file(file_path).exists
        assert host.file(file_path).is_file
        assert host.file(file_path).user == "vault"
        assert host.file(file_path).group == "vault"
        # Make sure it's not world- or group-readable
        mode = host.file(file_path).mode
        assert (mode & 0o7077) == 0


def test_service(host):
    service = host.service("vault.service")

    assert service.is_running
    assert service.is_enabled


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:8200").is_listening
