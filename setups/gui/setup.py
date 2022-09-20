#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from setuptools import setup

setup(
    name="decentra_network_gui",
    version="0.31.2",
    description="""This is GUI mode installer for Decentra Network""",
    url="https://docs.decentranetwork.org/",
    author="Decentra Network Developers",
    author_email="onur@decentranetwork.org",
    license="MPL-2.0",
    install_requires="""
Kivy==2.1.0
kivymd==0.104.2
kivymd_extensions.sweetalert==0.1.5
""",
    python_requires=">=3.8",
    zip_safe=False,
)
