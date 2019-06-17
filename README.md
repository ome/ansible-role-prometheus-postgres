Prometheus Postgres
===================

[![Build Status](https://travis-ci.org/ome/ansible-role-prometheus-postgres.svg)](https://travis-ci.org/ome/ansible-role-prometheus-postgres)
[![Ansible Role](https://img.shields.io/ansible/role/41324.svg)](https://galaxy.ansible.com/ome/prometheus_postgres)

Prometheus Postgres exporter.

This currently uses the local `postgres` administrator account on the PostgreSQL server.
In future this should be changed to use an unprivileged account.

See https://github.com/wrouesnel/postgres_exporter



Role Variables
--------------

All variables are optional:

- `prometheus_postgres_dbname`: The database name
- `prometheus_postgres_port`: Serve metrics on this port, default `9187`
- `prometheus_postgres_query_filenames`: A list of additional query files from `files/`, default `[queries-default.yml]`


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.prometheus_postgres
        prometheus_postgres_dbname: test


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
