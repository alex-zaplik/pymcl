from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pymcl",
    version="0.0.3",
    author="Alex Zaplik",
    author_email="zaplikpl@gmail.com",
    description="A set of Python bindings for the MCL library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex-zaplik/pymcl",
    packages=find_packages(include=['mcl', 'mcl.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
)
