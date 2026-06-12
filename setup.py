"""Installation script for the 'luwu_mjlab' python package."""

from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "mjlab==1.2.0",
    "mujoco-warp==3.5.0",
]

# Installation operation
setup(
    name="luwu_mjlab",
    packages=["src"],
    version="1.0.0",
    install_requires=INSTALL_REQUIRES,
)
