from setuptools import setup, find_packages

setup(
    name="calculator",
    description="This is my first library to calculate",
    version="1.0",
    packages=find_packages(include=['calculator']),
    author="Tarun",
    install_requires=['tqdm','pandas']
)