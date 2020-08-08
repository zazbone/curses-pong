py = venv/bin/python
pip = venv/bin/pip
venv = venv/bin/activate


run:
	$(py) -m curses-pong

build: install

install: inst-dep
	$(pip) install -e .

inst-dep:
	$(pip) install -r requirement.txt

test:
	$(py) test.py

freeze:
	$(pip) freeze > requirement.txt

py:
	$(py)

venv: FORCE
	source $(venv)

count:
	git ls-files | xargs wc -l

FORCE:
