Prometheus Postgres
===================

[![Actions Status](https://github.com/ome/ansible-role-prometheus-postgres/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-prometheus-postgres/actions)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-prometheus_postgres-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/ome/prometheus_postgres/)

Prometheus Postgres exporter.

This currently uses the local `postgres` administrator account on the PostgreSQL server.
In future this should be changed to use an unprivileged account.

See https://github.com/prometheus-community/postgres_exporter



Role Variables
--------------

All variables are optional:

- `prometheus_postgres_dbname`: The database name
- `prometheus_postgres_data_source_name`: implies `DATA_SOURCE_NAME` ENV variable in the [postgres_exporter](https://github.com/wrouesnel/postgres_exporter) 
- `prometheus_postgres_port`: Serve metrics on this port, default `9187`
- `prometheus_postgres_query_directory`: the directory containing query files which will be loaded by the exporter, default is `files/`
- `prometheus_postgres_query_filenames`: A list of additional query files from `prometheus_postgres_query_directory`, default `[queries-default.yml]`
- `prometheus_postgres_version`: the `postgres_exporter` version to be installed, default `0.4.6`
- `prometheus_postgres_sha256`: the SHA256 checksum of the `postgres_exporter` bundle of version `prometheus_postgres_version`, default: `9ed457c9a6d3a1e0132b3fe10f1d072457a667b009993a73e90b47ca99cc5bca`
- `prometheus_postgres_system_user`: The OS user used to run `postgres_exporter`, default: `postgres` (OS user is created only when differs from defaults).


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.prometheus_postgres
        prometheus_postgres_dbname: test


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
