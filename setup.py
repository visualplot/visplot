from setuptools import setup, find_packages

with open('README.md','r') as readme_file:
    readme = readme_file.read()

requirements = ['ipython>=6']

setup(
    name = 'visplot',
    version = '0.0.1',
    author = 'Upadhyay Ansh',
    author_email = 'anshumnupadhyay1@gmail.com',
    description = 'A package for the visualization',
    long_description=readme,
    url='https://github.com/visplot/upadhyayns/',
    packages=find_packages(),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)