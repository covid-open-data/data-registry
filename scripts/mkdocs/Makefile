.PHONY: pipenv_install
pipenv_install:
	pipenv install --dev


.PHONY: pip_install
pip_install:
	pip3 install -r requirements.txt


.PHONY: reqs_txt
reqs_txt:
	pipenv lock -r > requirements.txt


.PHONY: registry
registry:
	./mk_registry_docs.py ../../registry.yml ../../docs
