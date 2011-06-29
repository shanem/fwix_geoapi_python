#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "fwix_geoapi_python",
    version = "1.0",
    url = 'https://github.com/shanem/fwix_geoapi_python',
    download_url = 'git://github.com/shanem/fwix_geoapi_python.git',
    description = "The Fwix GeoAPI Python SDK",
    author = 'John Cwikla',
    packages = find_packages(),
    namespace_packages = ['fwix_geo_api', 'sample', 'test'],
    include_package_data = True,
)

