from setuptools import setup, find_packages
import os
import glob

requires = []

datadir = os.path.join('bunny_xbmc','workflow')



def get_datafiles(datadir):
    file_list = []
    for f in glob.glob(os.path.join(datadir, "*")):
        if not os.path.isdir(f):
            file_list.append(f)
        else:
            yield (f, get_datafiles(f))
    yield (datadir, file_list)



datafiles = list(get_datafiles(datadir))


print datafiles

setup(
    name = "bunny_xbmc",
    description='Framework to develop fancy xbmc apps fast.',
    version = "0.1",
    author = "Polynets Igor",
    packages=['bunny_xbmc'],
    entry_points={
        'console_scripts': [
            'bunny_create = bunny_xbmc.__init__:main',
        ],
    },
    include_package_data=True,
    data_files = datafiles,
  )
