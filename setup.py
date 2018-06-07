import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytwits",
    version="0.1",
    author="JACKSONMEISTER",
    author_email="therealjacksonmeister@gmail.com",
    description="pytwits is a Python wrapper for StockTwits' REST-API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JACKSONMEISTER/pytwits",
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
