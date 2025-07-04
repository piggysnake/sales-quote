"""
    This is a setup.py, py2app
    
"""
from setuptools import setup

APP = ['Desktop/Ben_quote/curtain_cal.py']
DATA_FILES = []
OPTIONS = {
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app']
    )
