from setuptools import setup, find_packages

setup(
    name="gitsense",
    version="0.1",
    packages=find_packages(),
    install_requires=["openai"],
    entry_points={
        "console_scripts": [
            "gitsense = gitsense.__main__:main"
        ]
    },
)
