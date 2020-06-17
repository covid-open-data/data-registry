# Make Docs

## Setup environment

- Create and activate python environment:
  - `pipenv --three`
  - `pipenv shell`
  - `make pipenv_install`

## Generate registry markdown file.

- Generate markdown file:
  - `pipenv shell`
  - `make registry`
  - Stage/commit/push changes in the [docs](../../docs) directory.

## Notes:

### GitHub Access
The [mk_registry_docs.py](mk_registry_docs.py) script requires the user running it to have SSH access to each repo in [registry.yml](../../registry.yml).

### Package Management
Use pipenv for managing packages. 
When a new package is added or removed run `make reqs_txt` to update the [requirements.txt](requirements.txt) file.

The [requirements.txt](requirements.txt) file is only needed and used by the GitHub Action.
