from setuptools import setup, find_packages

setup(
    name="fffa",  # lowercase, PyPI name
    version="0.1.1",
    author="Zeshan Khan",
    author_email="zeshankhanalvi@gmail.com ",
    description="FFFA: A Nature-Inspired Optimization Algorithm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zeshanalvi/FFFA",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
