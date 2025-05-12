from setuptools import find_packages, setup
from typing import List 

# Declaring variables for setup functions
def get_requirements() ->List[str]:

    """
    This function is going to return a list of requirements

    """

    requirement_list:List[str] = []

    """
    write a code to read the requirements.txt file and append the requirements to the requirement_list variable.

    """
    return requirement_list

setup(
    name = "flipkart",
    version = "0.0.1",
    author = "Nilesh",
    author_email = "nileshnv123@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

