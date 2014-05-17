from setuptools import setup

setup(
    name='soundatron',
    version='0.1dev',
    author='Ryan Small',
    author_email='ryan@foundatron.com',
    packages=['app'],
    license='LICENSE',
    description='Setup a bit perfect mpd server',
    long_description=open('README.md').read(),
    install_requires=[
        "Flask >=0.10.1",
        "Flask-Actions >=0.6.6",
        "Flask-WTF >=0.9.5",
        "Jinja2 >=2.7.2",
        "MarkupSafe >=0.19",
        "WTForms >=1.0.5",
        "Werkzeug >=0.9.4",
        "argparse >=1.2.1",
        "ipython >=2.0.0",
        "itsdangerous >=0.24",
        "wsgiref >=0.1.2",
    ],
)
