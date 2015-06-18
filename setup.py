from setuptools import setup

from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))


def read(name):
    with open(path.join(here, name), encoding='utf-8') as f:
        return f.read()

with open(path.join(here, 'oled/__init__.py'), 'r', encoding='utf-8') as f:
    __version__ = (re.search(r'__version__\s*=\s*u?"([^"]+)', f.read()).group(1).strip())

setup(
    name='mod-oled-128x64',
    version=__version__,
    description='Control module for MOD-OLED-128x64',
    long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
    url='https://github.com/SelfDestroyer/pyMOD-OLED',
    author='Stefan Mavrodiev',
    author_email='support@olimex.com',
    license='GPL2',

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Topic :: Scientific/Engineering :: Visualization",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='oled OLinuXino',

    install_requires=['smbus-cffi'],
    packages = ['oled'],
    platforms='ARM'

)