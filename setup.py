import re
from os import path

from setuptools import setup

# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# read the version file
VERSIONFILE = "cocoviewer/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
mo = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
if not mo:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
version_str = mo.group(1)

setup(
    name="cocoviewer",
    version=version_str,
    description="View coco format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tin Lai (@soraxas)",
    author_email="oscar@tinyiu.com",
    license="MIT",
    url="https://github.com/soraxas/coco-viewer",
    python_requires=">=3.6",
    # packages=[
    #     "termplot",
    #     "termplot.backend",
    #     "termplot.data_source",
    # ],
    # install_requires=[
    #     "tensorboard>=2.5",
    #     "plotext==5.0.2",
    #     "mock",
    #     "pandas",
    #     "numpy",
    #     "scipy",
    #     "argcomplete",
    #     "watchdog",
    # ],
    entry_points={
        "console_scripts": [
            "coco-viewer=cocoviewer.cocoviewer:main",
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Desktop Environment",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
)
