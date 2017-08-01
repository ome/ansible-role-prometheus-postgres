Prometheus Postgres
===================

Prometheus Postgres exporter.

This currently uses the local `postgres` administrator account on the PostgreSQL server.
In future this should be changed to use an unprivileged account.

See https://github.com/wrouesnel/postgres_exporter



Role Variables
--------------

All variables are optional:

- `prometheus_postgres_dbname`: The database name
- `prometheus_postgres_port`: Serve metrics on this port, default `9187`


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: prometheus-postgres
        prometheus_postgres_dbname: test


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
