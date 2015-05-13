import os.path
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = "0.2"

setup(
    name = "python-recsys",
    version = VERSION,
    description="A simple recommender system in python",
    author='Oscar Celma',
    author_email='ocelma@bmat.com',
    maintainer='Raefer Gabriel',
    maintainer_email='raefer@delvv.com',
    license = "http://www.gnu.org/copyleft/gpl.html",
    platforms = ["any"],    
    url="https://github.com/delvv/python-recsys",
    download_url = 'https://github.com/delvv/python-recsys/archive/0.2.zip',
    package_dir={'recsys':'recsys'},
    packages=['recsys', 'recsys.algorithm', 'recsys.datamodel', 'recsys.evaluation', 'recsys.utils'],
    install_requires = ["numpy", "scipy", "divisi2", "csc-pysparse"],
)
