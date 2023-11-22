activate:
	source venv/bin/activate


test:
	python -m unittest discover -p '*_test.py'



.PHONY: test activate
