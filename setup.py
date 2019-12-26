#!/usr/bin/env python3
# flake8: noqa

from setuptools import setup

setup(
    name="wpa_status",
    version="0.0.1",
    description="client library for wpa_statusd",
    author="Alex Fence",
    packages=["wpa_status"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)"
    ]
)
