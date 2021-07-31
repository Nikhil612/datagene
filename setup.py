from setuptools import find_packages, setup


def read_reqs(req_file: str):
    with open(req_file) as req:
        return [
            line.strip()
            for line in req.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]


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
