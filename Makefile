# Directories
dirs:
	mkdir data
	mkdir src
	mkdir scripts
	mkdir notebooks
	mkdir analysis

# Environment
venv: requirements.txt
	python3 -m venv venv
	source venv/bin/activate && \
	python3 -m pip install -r requirements.txt
