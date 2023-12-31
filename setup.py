from setuptools import setup, find_packages
from python_version import min_python_version

min_version = min_python_version()
min_version_str = '.'.join(str(num) for num in min_version)

setup(
    name="remote",
    version="0.1",
    packages=find_packages(),
    author="Louis-Vincent Grand'Maison",
    author_email="grandmaison.lv@gmail.com",
    description="A package designed to facilitate the manipulation of remote sensing data in python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gmlouis/remote",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows :: Windows 10",
        "Topic :: Scientific/Engineering :: Photogrammetry",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Remote Sensing",
        "Topic :: Scientific/Engineering :: Hyperspectral Imagery",
    ],
    python_requires='>={}'.format(min_version_str)
)