include common.mk
LINTER = flake8
API_DIR = server
DB_DIR = data
REQ_DIR = .

PKG = $(API_DIR)
PYTESTFLAGS = -vv --verbose --cov-branch --cov-report term-missing --tb=short -W ignore::FutureWarning

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

all_tests: FORCE
	cd $(API_DIR); pytest $(PYTESTFLAGS) --cov=$(API_DIR)
	cd $(DB_DIR); pytest $(PYTESTFLAGS) --cov=$(DB_DIR)

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd $(API_DIR); make docs
