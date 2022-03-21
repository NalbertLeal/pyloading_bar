import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="pyloading_bar",
  packages=['pyloading_bar'],
  version="0.0.1",
  author="Nalbert Gabriel Melo Leal",
  author_email="nalbertgml@gmail.com",
  description="A python loading bar to use in terminal applications",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/NalbertLeal/pyloading_bar",
  project_urls={
    "Bug Tracker": "https://github.com/NalbertLeal/pyloading_bar/issues",
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
  ],
  python_requires=">=3.8",
)