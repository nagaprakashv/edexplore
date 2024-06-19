from setuptools import setup, find_namespace_packages
from glob import glob
from os import path

# Get the version from Version.txt
vers = path.abspath(path.dirname(__file__))
with open(path.join(vers, 'VERSION.txt'), encoding='utf-8') as f:
    __version__ = f.read()

setup(name='edexplore',
      version=__version__,
      description='A simple widget for interactive data exploration for those who use Pandas in Jupyter Notebook.',
      install_requires=['requests', 'numpy', 'pandas', 'ipywidgets'],
      url='https://github.com/nagaprakashv/explore/',
      author='nagaprakash venkatesan',
      author_email='npv3105@outlook.com',
      packages=find_namespace_packages(),
      include_package_data=True,
      zip_safe=False)
