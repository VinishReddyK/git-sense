from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gitsense",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered Git assistant for smarter version control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gitsense",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "google-generativeai>=0.3.0",
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