from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mod-oled-128x64',
    version='1.0.0b1',
    description='Control module for MOD-OLED-128x64',
    long_description=long_description,
    url='',
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

    keywords='oled',

    install_requires=['pyserial'],
    packages = ['oled'],
    platforms='arm'

)