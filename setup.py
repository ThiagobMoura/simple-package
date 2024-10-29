from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="first_package",
    version="0.0.1",
    author="Thiago_Moura",
    author_email="thiagobat.mr@gmail.com",
    description="Prpjeto DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThiagobMoura/simple-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
