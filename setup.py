from setuptools import setup, find_packages

requires = []

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
    package_data={'bunny_xbmc': ['workflow/appname/*', 'workflow/bunny/*', 'workflow/resources/*', 'workflow/*']},
    include_package_data=True,
  )
