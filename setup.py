from setuptools import setup, find_packages


def read_requirements() -> list:
    """simple function to read the requirements
    file and add them as a list into the
    install_requires of the CLI

    Returns:
        list: [list of libs that the CLI needs]
    """

    with open("docs/requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


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
    name="rdap",
    version="0.1.4",
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
    python_requires=">=3.6",
    install_requires=read_requirements(),
    packages=get_packages(),
)
