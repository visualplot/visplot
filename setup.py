from setuptools import setup, find_packages

with open('README.md','r') as readme_file:
    readme = readme_file.read()

requirements = ['ipython>=6']

setup(
    name = 'visplot',
    version = '0.0.1',
    author = 'upadhyayans',
    author_email = 'Upadhyay Ansh',
    description = 'A package for the visualization',
    long_description=readme,
    long_description_content_type = 'type/markdown',
    url='https://github.com/visplot/upadhyayns/',
    packages=find_packages(),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
)