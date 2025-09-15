# Filename Makefile

# Phython info
PYTHON = python3

# Pylint info
PYLINT = $(PYTHON) -m pylint
PYLINT_FLAGS := --rcfile=.pylintrc

# Deployment info
SERVERS ?= 9.99.99.99

# Recipies
.PHONY: lint
lint:
	@echo "Running Lint check"
	@echo "Repository:$$repository_url"
	@echo "Workspace:$$workspace"
	@$(PYLINT) $(PYLINT_FLAGS) $$workspace/testcases
	@echo "Linting Completed"

.PHONY: deploy
deploy:
	@echo "***Configuring repository for deployment***"
#	@git config core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
	@echo "***Starting deployment***"
	@echo "Servers: $(SERVERS)"
#	@for server in $(SERVERS) ; do \
#		echo "***Pushing changes to $$server***"; \
#		git push ilab@$$server:/home/ilab/git/iLabConfig master:master; \
#	done
