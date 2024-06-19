from setuptools import setup, find_namespace_packages
from glob import glob

setup(name='edexplore',
      version="1.0.0",
      description='A simple widget for interactive data exploration for those who use Pandas in Jupyter Notebook.',
      install_requires=['requests', 'numpy', 'pandas', 'ipywidgets'],
      url='https://github.com/nagaprakashv/edexplore/',
      author='nagaprakash venkatesan',
      author_email='npv3105@outlook.com',
      packages=find_namespace_packages(),
      include_package_data=True,
      zip_safe=False)