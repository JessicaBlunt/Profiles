import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="profiles",
    version="0.0.1",
    author="Jessica Blunt, Tyler Bell, Brian Greene",
    author_email="jessica.m.blunt-1@ou.edu",
    description="Tools to process atmospheric data collected by UAS along either vertical or horizontal lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oucass/Profiles",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: TBD",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
