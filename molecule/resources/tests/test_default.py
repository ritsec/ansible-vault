import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_user(host):
    user = host.user("vault")

    assert user.exists
    assert user.gecos == "HashiCorp Vault"
    # Not fantastic test to make sure it's a system account instead of a user account
    assert user.uid < 1000
    assert user.gid < 1000
    assert user.group == "vault"


def test_service(host):
    service = host.service("vault.service")

    assert service.is_running
    assert service.is_enabled


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:8200").is_listening
