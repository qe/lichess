from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="lichess",
    version="0.1.2",
    description="Python Lichess API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qe/lichess",
    author="Alex Ismodes",
    author_email="helloemailmerighthere@gmail.com",
    install_requires=[""],
    license="MIT",
    keywords="lichess chess api wrapper",
    project_urls={
        "Documentation": "https://lichess.readthedocs.io",
        "Issue Tracker": "https://github.com/qe/lichess/issues",
        "Source Code": "https://github.com/qe/lichess",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=["lichess"],
    )