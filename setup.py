from setuptools import setup

setup(
    name='lichess',
    version='0.1.1',
    description='A Python wrapper for the Lichess API',
    url='http://github.com/qe/lichess',
    author='Alex Ismodes',
    author_email='helloemailmerighthere@gmail.com',
    license='MIT',
    classifiers=[
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
    keywords='lichess chess api',
    packages=['lichess'],
    install_requires=[''],
    )