try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='freecurrencyapi',
    version='0.1.0',
    packages=['freecurrencyapi'],
    url='https://github.com/everapihq/freecurrencyapi-python',
    license='MIT',
    author='Everapi',
    author_email='office@everapi.com',
    description='Freecurrencyapi Python Client',
    keywords = ['free currency api', 'exchange rates', 'rates api', 'freecurrencyapi', 'currency api'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "requests",
        "everapi"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
