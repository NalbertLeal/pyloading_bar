build:
	rm -r dist/
	rm -r build/
	python setup.py bdist_wheel
test:
	python -m unittest -v
testpypi:
	py -m twine upload --repository testpypi dist/*
pypi:
	py -m twine upload --repository pypi dist/*