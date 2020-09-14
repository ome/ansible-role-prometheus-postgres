import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_services_running_and_enabled(host):
    assert host.service('prometheus-postgres-exporter').is_running
    assert host.service('prometheus-postgres-exporter').is_enabled


def test_node_exporter_metrics(host):
    out = host.check_output('curl http://localhost:19187/metrics')
    assert (
        'pg_database_size{datname="alice",server="/var/run/postgresql/:5432"}'
    ) in out
