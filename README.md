<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="300"/>
</p>

[![build](https://github.com/silentsokolov/dbt-databend/actions/workflows/build.yml/badge.svg)](https://github.com/silentsokolov/dbt-databend/actions/workflows/build.yml)

## dbt-databend

The `dbt-databend` package contains all of the code enabling [dbt](https://getdbt.com) to work with [Databend](https://databend.rs/).

## Getting started

- [Install dbt](https://docs.getdbt.com/docs/installation)
- Read the [introduction](https://docs.getdbt.com/docs/introduction/) and [viewpoint](https://docs.getdbt.com/docs/about/viewpoint/)

### Installation

Use your favorite Python package manager to install the app from PyPI, e.g.

```bash
python -m pip install dbt-databend
```

### Supported features

Databend does not support a `ALTER` query for change a tables schema. So some features are not available.

- [x] Table materialization
- [x] View materialization
- [ ] Incremental materialization
- [x] Seeds
- [x] Sources
- [x] Docs generate
- [ ] Tests
- [ ] Snapshots
- [ ] Ephemeral materialization

### Database & schema

The dbt model `database.schema.table` is not compatible with Databend because Databend does not support a `schema`.
So we use a simple model `schema.table`, where `schema` is the Databend's database.

### Configuration

| Option     | Description                                                                                                                                            | Required?              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| cluster_by | For detailed information about the CLUSTER BY clause, see [SET CLUSTER KEY](https://databend.rs/doc/reference/sql/ddl/clusterkey/dml-set-cluster-key). | Optional (default: `empty`) |

### Profile Configuration

Databend targets should be set up using the following configuration in your `profiles.yml` file.
The `dbt-databend` package usage mysql-procotol for connect to database.

```yaml
your_profile_name:
  target: dev
  outputs:
    dev:
      type: databend
      host: [hostname]
      port: [port]  # default 3307
      user: [username]
      password: [password]
      schema: [database name]
```
