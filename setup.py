from setuptools import setup, find_packages
import os
import glob

requires = []

datadir = os.path.join('bunny_xbmc','workflow')

datafiles = [(root, [os.path.join(root, f) for f in files) for root, dirs, files in os.walk(datadir)]

def get_datafiles(datadir):
    datadirs = [datadir]
    result = []
    def pars_folder(datadir):
        file_list = []
        folders = []
        for f in glob.glob(os.path.join(datadir, "*")):
            if not os.path.isdir(f):
                file_list.append(f)
            else:
                folders.append(f)
            return file_list, folders

    while datadirs.len():
        for dr in datadirs
            file_list, dirs = pars_folder(datadirs)
            result.append((dr, filelist))
            datadirs.extend()

    return result



datafiles = get_datafiles(datadir)


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