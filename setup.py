from distutils.core import setup
import os
import glob

requires = []

datadir = os.path.join('bunny_xbmc', 'workflow')

datafiles = [(root, [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk(datadir)]

setup(
    name="bunny_xbmc",
    description='Framework to develop fancy xbmc apps fast.',
    version="0.1",
    author="Polynets Igor",
    packages=['bunny_xbmc'],
    entry_points={
        'console_scripts': [
            'bunny_create = bunny_xbmc.__init__:bunny_crate',
            'bunny_repo = bunny_xbmc.__init__:bunny_repo',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    package_data = {
               'workflow/': ['*.tmplt'],
               'workflow/resources': ['*.xml'],
               'workflow/resources/skins/DefaultSkin/720p': ['*.xml'],
               'workflow/resources/skins/DefaultSkin/media': ['*.jpg'],
               },
    data_files = datafiles,
  )
