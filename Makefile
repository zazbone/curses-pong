py = venv/bin/python
pip = venv/bin/pip


run:
	$(py) -m curses-pong

build: install

install: inst-dep
	$(pip) install -e .

inst-dep:
	$(pip) install -r requirement.txt

freeze:
	$(pip) freeze --all > requirement.txt

py:
	$(py)
