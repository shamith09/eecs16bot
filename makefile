setup:
	@pip install pip --upgrade
	@pip install -r bin/requirements.txt

grade:
	@python3 src/main.py
