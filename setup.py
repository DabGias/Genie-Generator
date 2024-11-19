from setuptools import setup


setup(
    name = "genie",
    version = "0.0.1",
    py_modules = [
        "main", 
        "utils"
    ],
    install_requires = [
        "Click",
    ],
    entry_points = {
        "console_scripts": ["gen = main:gen"]
    }
)
