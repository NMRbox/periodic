from setuptools import setup,find_packages
#from distutils.core import setup
import os

def read(fname):  
    fpath = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), fname)
    with open(fpath, 'r') as fhandle:
        return fhandle.read()
    
setup(
    name = "periodic2023",
    version = '2.2.1',
    author = 'Jose Luis Naranjo Gomez',
    author_email = 'luisnaranjo733@hotmail.com',
    maintainer = 'Gerard Weatherby / NMRbox',
    maintainer_email = 'gweatherby@uchc.edu',
    description = ("A periodic table API."),
    license = "GNU GPL",
    keywords = "chem chemistry periodic table finder elements",
    #url = "https://github.com/doubledubba/periodic",
    url = "https://github.com/NMRbox/periodic.git",
    packages = ['periodic'],
    #package_data = {'periodic': ['table.db']}
    include_package_data = True,
    entry_points = {
    'console_scripts': ['periodic = periodic.table:interactive_shell']
    },
    install_requires = ['SQLAlchemy==0.7.7'],
    long_description=read('README.rst'),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Utilities",
    ],

)
