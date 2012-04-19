from setuptools import setup, find_packages

requires = []

setup(
    name = "bunny_xbmc",
    description='eTV censore processor',
    version = "0.1",
    author = "Polynets Igor",
    packages=['bunny_xbmc'],
    entry_points={
        'console_scripts': [
            'bunny_create = bunny_xbmc.__init__:main',
        ],
    },
    include_package_data=True,
  )
