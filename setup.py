from setuptools import find_packages
from setuptools import setup

setup(
    name='profiler',
    version='0.0',
    description='Profiler',
    url='https://gitlab.rdcloud.intra.hitachi.co.jp/71389710/profiler',
    author='Honoka',
    author_email='terufumi.morishita.wp@hitachi.com',
    license='Hitachi R&D',
    install_requires=[
        'line-profiler'
    ],
    packages=find_packages(),
    zip_safe=False,
)
