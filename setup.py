import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='python-mailerlite',
    version='0.1',
    author='Cam Fulton',
    author_email='jcameronfulton@gmail.com',
    license='MIT',
    url='https://github.com/LarryBrid/python-mailerlite',
    download_url='https://github.com/LarryBrid/python-mailerlite/tarball/0.1',
    keywords='mailerlite api',
    description='A Python wrapper around the MailerLite API',
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Email',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
