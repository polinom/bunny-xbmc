from setuptools import setup, find_packages
import os
import glob

requires = []

datadir = os.path.join('bunny_xbmc','workflow')

datafiles = [(root, [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk(datadir)]

setup(
    name = "bunny_xbmc",
    description='Framework to develop fancy xbmc apps fast.',
    version = "0.1",
    author = "Polynets Igor",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bunny_create = bunny_xbmc.__init__:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    #data_files = datafiles,
  )