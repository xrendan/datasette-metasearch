from setuptools import setup
import os

VERSION = "0.10.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-metasearch",
    description="Build a search index across content from multiple SQLite database tables and run faceted searches against it using Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/dogsheep/beta",
    project_urls={
        "Issues": "https://github.com/dogsheep/beta/issues",
        "CI": "https://github.com/dogsheep/beta/actions",
        "Changelog": "https://github.com/dogsheep/beta/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_metasearch"],
    package_data={"datasette_metasearch": ["templates/*.html"]},
    entry_points={
        "datasette": ["beta = datasette_metasearch"],
        "console_scripts": ["datasette-metasearch = datasette_metasearch.cli:cli"],
    },
    install_requires=["datasette>=0.50.2", "click", "PyYAML", "sqlite-utils>=3.0"],
    extras_require={
        "test": ["pytest", "pytest-asyncio", "httpx", "beautifulsoup4", "html5lib"]
    },
    tests_require=["datasette-metasearch[test]"],
)
