import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTwits",
    version="1.0.1",
    author="Tim Bienias",
    author_email="",
    description="PyTwits is a REST-API Wrapper for StockTwits.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbienias/PyTwits",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
