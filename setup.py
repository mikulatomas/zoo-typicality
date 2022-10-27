from setuptools import setup, find_packages

from mini_zoo_concepts import __version__, __author__, __email__

setup(
    name="mini_zoo_concepts",
    version=__version__,
    description="",
    long_description="",
    url="https://github.com/mikulatomas/zoo-typicality",
    author=__author__,
    author_email=__email__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
    ],
    classifiers=["Development Status :: 1 - Planning"],
)
