# Changelog

# 0.4.3-2globo

- Rollback exposing nic node information

# 0.4.3-1globo

- Add get_vm function to retrieve VM information
- Fix _get_node_for_id to retrieve node information
- Expose nic node information

# 0.4.3

- Update pack so it also works with providers such as Vultr which only take a single credential
  argument - either ``api_key`` or ``api_secret``. Previously it only worked with providers which
  took both.

# 0.4.0

- Updated action `runner_type` from `run-python` to `python-script`

## v0.3.0

* Migrate to `config.schema.yaml`

## v0.2.0

* Exoscale provider
  [Sebastien Goasguen]

## v0.1.0

* Initial release
