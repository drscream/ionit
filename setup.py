#!/usr/bin/python3

# Copyright (C) 2018-2022, Benjamin Drung <bdrung@posteo.de>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""Setup for ionit"""

import subprocess

from setuptools import setup


def systemd_unit_path():
    """Determine path for systemd units"""
    try:
        command = ["pkg-config", "--variable=systemdsystemunitdir", "systemd"]
        path = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return path.decode().replace("\n", "")
    except (subprocess.CalledProcessError, OSError):
        return "/lib/systemd/system"


if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as fh:
        LONG_DESCRIPTION = fh.read()

    setup(
        name="ionit",
        version="0.4.1",
        description="Render configuration files from Jinja templates",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Benjamin Drung",
        author_email="bdrung@posteo.de",
        url="https://github.com/bdrung/ionit",
        project_urls={"Bug Tracker": "https://github.com/bdrung/ionit/issues"},
        license="ISC",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "License :: OSI Approved :: ISC License (ISCL)",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        install_requires=["jinja2", "PyYAML"],
        scripts=["ionit"],
        py_modules=["ionit_plugin"],
        data_files=[(systemd_unit_path(), ["ionit.service"])],
        python_requires=">=3.6",
    )
