from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="GitSense",
    version="0.1.0",
    author="Vinish Reddy Kamireddy",
    author_email="vinishreddy.k@gmail.com",
    description="A CLI/desktop tool that uses AI to automate and enhance common Git workflows, making version control smarter and more intuitive.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VinishReddyK/git-sense",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "python-dotenv",
        "google-generativeai",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "gitsense=gitsense.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Version Control :: Git",
        "Environment :: Console",
    ],
    keywords="git ai llm productivity developer-tools",
)