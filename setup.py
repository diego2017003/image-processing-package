from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="diego",
    author_email="diego25rn@gmail.com",
    description="package to process images with opencv",
    long_description=page_description,
    long_description_content_type="package to process images with opencv and extract rois with pdi processing",
    url="https://github.com/diego2017003/image-processing-package"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11',)
