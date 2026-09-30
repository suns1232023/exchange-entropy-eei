from setuptools import setup, find_packages

setup(
    name="eei",
    version="0.1.0",
    author="Scott Sun",
    description="Exchange Entropy Index (EEI) Core Package",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.22.0",
        "pandas>=1.4.0",
        "scipy>=1.8.0",
    ],
)
