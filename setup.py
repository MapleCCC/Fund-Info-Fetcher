import setuptools

from fetcher import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fund Info Fetcher",
    author="MapleCCC",
    author_email="littlelittlemaple@gmail.com",
    description="A script to fetch various fund information from "
    "fund.eastmoney.com, and structuralize into Excel document.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MapleCCC/Fund-Info-Fetcher",
    version=__version__,
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=open("requirements/install.txt", "r").read().splitlines(),
    entry_points={"console_scripts": ["fetcher=fetcher.__main__:main",]},
)
