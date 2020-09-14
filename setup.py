# https://packaging.python.org/guides/making-a-pypi-friendly-readme/

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='psgui_util',
    version='0.1',
    description='PySimpleGUI Utility Library',
    url='https://github.com/javacommons/psgui_util',
    author='javacommons',
    author_email='javacommons@gmail.com',
    license='MIT',
    keywords='development',
    packages=[
        "psgui_util",
    ],
    install_requires=["PySimpleGUI>=4.29.0"],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
