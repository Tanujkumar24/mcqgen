#we use setup.py file , for installing the local package in my virtual environment
from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Tanujkumar',
    author_email='tanuj.mangalapally@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
#where ever you find __init__.py , it will consider it as a package