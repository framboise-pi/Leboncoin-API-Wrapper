from setuptools import setup

setup(
    name='leboncoin-api-wrapper',
    url="https://github.com/Shinyhero36/Leboncoin-API-Wrapper",
    version='0.1',
    license='GNU General Public License v3.0',
    install_requires=[
        'requests >= 2.25.0',
        'cloudscraper >= 1.2.48',
    ],
    author="Shinyhero36",
    setup_requires=['setuptools_scm'],  # Automatically include Ressources files
    include_package_data=True,
    packages=['leboncoin_api_wrapper'],
)
