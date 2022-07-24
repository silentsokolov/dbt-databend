#!/usr/bin/env python

import re
from os.path import dirname, join

from setuptools import find_namespace_packages, setup


# get this from a separate file
def _dbt_databend_version():
    _version_path = join(dirname(__file__), "dbt", "adapters", "databend", "__version__.py")
    _version_pattern = r"""version\s*=\s*["'](.+)["']"""
    with open(_version_path, encoding="utf-8") as f:
        match = re.search(_version_pattern, f.read().strip())
        if match is None:
            raise ValueError(f"invalid version at {_version_path}")
        return match.group(1)


package_name = "dbt-databend"
package_version = _dbt_databend_version()
description = """The Databend plugin for dbt (data build tool)"""

dbt_version = "1.1"

if not package_version.startswith(dbt_version):
    raise ValueError(
        f"Invalid setup.py: package_version={package_version} must start with "
        f"dbt_version={dbt_version}"
    )


setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=open(join(dirname(__file__), "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Dmitriy Sokolov",
    author_email="silentsokolov@gmail.com",
    url="https://github.com/silentsokolov/dbt-databend",
    license="MIT",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    package_data={
        "dbt": [
            "include/databend/dbt_project.yml",
            "include/databend/macros/*.sql",
            "include/databend/macros/**/*.sql",
        ]
    },
    install_requires=[
        f"dbt-core~={dbt_version}",
        "mysql-connector-python>=8.0.0,<8.1",
    ],
    python_requires=">=3.7",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "dbt",
        "databend",
    ],
)
