from setuptools import setup

setup(name='gf_python',
      version='0.1',
      description='Utilities to work with GF trees from Python',
      url='http://github.com/smucclaw/gf-python',
      author='Inari Listenmaa',
      author_email='',
      license='',
      packages=['gf_python'],
      install_requires=['pgf',
          'yaml',
          'pyparsing'
          ],
      zip_safe=False)
