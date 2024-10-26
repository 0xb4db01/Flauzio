from setuptools import setup

setup(
    name='Flauzio',
    description='A tiny modular python web server with ssl support',
    version='0a1',
    author='0xb4db01',
    packages=[
        'flauzio',
        'flauzio.api',
    ],
    entry_points={
        'console_scripts':[
            'flauzio=flauzio.flauzio:main',
        ]
    }
)
