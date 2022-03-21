from distutils.core import setup

setup(
  name = 'pyloading',         # How you named your package folder (MyLib)
  packages = ['pyloading'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='Apache 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python loading bar to use in terminal applications',   # Give a short description about your library
  author = 'nalbert Gabriel Melo Leal',                   # Type in your name
  author_email = 'nalbertgml@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/NalbertLeal/pyloading',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/NalbertLeal/pyloading/archive/refs/tags/v0.1.tar.gz',    # I explain this later on
  keywords = ['python', 'loading bar', 'CLI', 'terminal'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache 2.0 License',
    'Programming Language :: Python :: 3.8',
  ],
)