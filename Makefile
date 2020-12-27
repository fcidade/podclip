run:
	./.env/bin/python3 .

unit-test:
	python3 -m unittest discover test/
