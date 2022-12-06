from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in a3jobs/__init__.py
from a3jobs import __version__ as version

setup(
	name="a3jobs",
	version=version,
	description="Recruitment Platform",
	author="Muhammed Rahid V K",
	author_email="muhammed.rahid.v.k@acube.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
