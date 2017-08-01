import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_services_running_and_enabled(Service):
    assert Service('prometheus-postgres-exporter').is_running
    assert Service('prometheus-postgres-exporter').is_enabled


def test_node_exporter_metrics(Command):
    out = Command.check_output('curl http://localhost:19187/metrics')
    assert 'pg_database_size{datname="alice"}' in out
