build:
	rm -r dist/
	rm -r build/
	python setup.py bdist_wheel
pypi:
	py -m twine upload --repository testpypi dist/*