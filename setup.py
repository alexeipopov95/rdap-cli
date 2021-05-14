from setuptools import setup, find_packages


INSTALL_REQUIREMENTS = ["click", "requests", "pytest"]
PACKAGES = ["rdap"] + [
    "rdap.{0}".format(package) for package in find_packages("rdap")
]


setup(
    name = "rdap",
    version = "0.0.1",
    author = "Alexei Popov",
    author_email = "",
    entry_points = {
        "console_scripts" : [
            "rdap=rdap.rdap:cli",
        ]
    },
    description= (
        "A simple CLI designed to offer a quick way of gathering domain"
        "data information. And for practicing."
    ),
    python_requires=">=3.6",
    install_requires = INSTALL_REQUIREMENTS,
    packages = PACKAGES
)

"""
setup(
    name = "rdap",
    version = "0.0.1",
    author = "Alexei Popov",
    author_email = "",
    py_modules=['rdap'],
    install_requires=[
        'Click',
        'requests',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'rdap = rdap.rdap:cli',
        ],
    },
)
"""