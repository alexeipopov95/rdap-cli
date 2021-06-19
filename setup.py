from setuptools import setup, find_packages


def get_packages() -> list:
    """simple function designed to return a list
    of packages involved in our CLI

    Returns:
        list: [package list]
    """

    root = ["rdap"]
    package_list = ["rdap.{0}".format(package) for package in find_packages(root[0])]
    return root + package_list


setup(
    name="rdap-cli",
    version="1.0.0",
    author="Alexei Popov",
    author_email="alexei.popov.cli@gmail.com",
    entry_points={
        "console_scripts": [
            "rdap=rdap.rdap:cli",
        ]
    },
    description=(
        "A simple CLI designed to offer a quick way of gathering domain"
        "data information."
    ),
    url="https://github.com/alexeipopov95/rdap-cli",
    download_url=(
        "https://github.com/alexeipopov95/rdap-cli/archive/refs/tags/1.0.0.tar.gz"
    ),
    keywords=["rdap", "cli", "whois", "registration-date", "data", "domain"],
    python_requires=">=3.6",
    install_requires=[
        "black==21.6b0",
        "click==8.0.1",
        "flake8==3.9.2",
        "pre-commit==2.13.0",
        "python-dateutil==2.8.1",
        "PyYAML==5.4.1",
        "requests==2.25.1",
        "tabulate==0.8.9",
        "tldextract==3.1.0",
        "validators==0.18.2",
    ],
    packages=get_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
