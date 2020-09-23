from setuptools import setup, find_packages

setup(
    name='gsextract',
    version='0.1',
    packages=find_packages(),
    #py_modules=['gsextract'],
    setup_requires=['wheel'],
    install_requires=[
        'kaitaistruct',
        'click',
        'scapy'
    ],
    entry_points='''
        [console_scripts]
        gsextract=gsextract.gsextract:cli_runner
    ''',
)
