from setuptools import setup, find_packages

setup(
    name='some_package_proj',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
