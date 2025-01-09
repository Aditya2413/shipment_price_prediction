from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function is used to get the requirements from the file.
    Args:
    file_path : str : file path of the requirements.txt file.
    Returns:
    List[str] : list of requirements.
    """
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"")for req in requirements]
        
        return requirements
    

setup(
    name='Shipment_price_predication',
    version='0.1',
    author='Aditya ugale',
    author_email="adityaugale4652@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requriements.txt')
)