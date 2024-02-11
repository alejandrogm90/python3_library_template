from setuptools import setup, find_packages

setup(
    name="python3_template",
    version="1.0",
    description="Python3 template example",
    long_description=open('README.md').read(),
    author="Alejandro Gómez",
    author_email="alejandrogomezmartin90@outlook.com",
    license='MIT',
    packages=[
        "src",
        "src/utils",
        "config",
        "log",
    ],
    install_requires=find_packages()
)
