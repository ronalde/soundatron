from setuptools import setup

setup(
    name='soundatron',
    version='0.1dev',
    author='Ryan Small',
    author_email='ryan@foundatron.com',
    packages=['soundatron'],
    license='LICENSE',
    description='Setup a bit perfect mpd server',
    long_description=open('README.txt').read(),
    install_requires=[
        "Flask >=0.10.1",
    ],
)
