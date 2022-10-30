from setuptools import setup, find_namespace_packages

setup(name='blover',
      version='1.6',
      description='Python blover Utilities',
      author='mMukati',
      author_email='mm@polyuno.com',
      url='https://github.com/momomukati/basicpackage',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src')
     )