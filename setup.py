from setuptools import find_packages
from setuptools import setup

setup(
    name='line_profiling',
    version='0.0',
    description='Line Profiling',
    author='Honoka',
    install_requires=[
        'line-profiler'
    ],
    packages=find_packages(),
    zip_safe=False,
)
