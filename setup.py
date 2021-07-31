from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="datagene",
    packages=find_packages(),
    author="Nikhil Joshi",
    author_email="joshi.nikh@northeastern.edu",
    url="https://github.com/Nikhil612/datagene",
    description=(
        "A Fastest way to generate tabular data and train it on Auto Ml Architecture "
    ),
    license="MIT",
    packages=["datagene"]
    install_requires=read_reqs("requirements.txt"),
    include_package_data=True,
    version="1.0.0",
    zip_safe=False,
)
