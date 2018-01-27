import os.path
import sys

import setuptools

root_dir = os.path.abspath(os.path.dirname(__file__))

description = "Roslibpy"

readme_file = os.path.join(root_dir, 'README.rst')
with open(readme_file, encoding='utf-8') as f:
    long_description = f.read()

version_module = os.path.join(root_dir, 'roslibpy', 'version.py')
with open(version_module, encoding='utf-8') as f:
    exec(f.read())

py_version = sys.version_info[:2]

if py_version < (3, 6):
    raise Exception("roslibpy requires Python >= 3.5.")

packages = [
        'roslibpy',
        'roslibpy.actionlib',
        'roslibpy.math',
        'roslibpy.tf',
        'roslibpy.urdf']

setuptools.setup(
        name='roslibpy',
        version=version,
        description=description,
        long_description=long_description,
        url='https://github.com/mortenmj/roslibpy',
        author='Morten Mjelva',
        author_email='morten.mjelva@gmail.com',
        license='BSD',
        packages=packages,
        include_package_data=True,
)
