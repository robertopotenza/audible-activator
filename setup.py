from setuptools import setup, find_packages

setup(
    name="audible-activator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "audible-activator=audible_activator.main:main",
        ],
    },
)
