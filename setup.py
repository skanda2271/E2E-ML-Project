from setuptools import setup, find_packages
from typing import List

CONDITION = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """This will return the list of requirements"""
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if CONDITION in requirements:
            requirements.remove(CONDITION)
    return requirements

setup(
   name="my_package",
   version="0.1.0",
   author="Skanda Smaran Vasudevan",
   author_email="skandasmaran2271@gmail.com",
   description="A sample Python package",
   long_description=open("README.md").read(),
   long_description_content_type="text/markdown",
   url="https://github.com/skanda2271/E2E-ML-Project",
   packages=find_packages(),
   install_requires=get_requirements("requirement.txt"),
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License"
   ],
   python_requires='>=3.7',
)

