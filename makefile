clean:
	rm -r dist/
	rm -r build/
	pyloading_bar.egg-info/
build:
	python setup.py bdist_wheel
test:
	python -m unittest -v
testpypi:
	python -m twine upload --repository testpypi dist/*
pypi:
	python -m twine upload --repository pypi dist/*