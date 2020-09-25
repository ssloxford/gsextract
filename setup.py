from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gsextract',
    version='1.0',
    author='James Pavur',
    author_email='james.pavur@cs.ox.ac.uk',
    description='A tool to parse corrupted recordings of satellite internet traffic in the GSE over DVB-S format into .pcaps',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssloxford/gsextract",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Security"
    ],
    python_required='>=3.7',
    packages=find_packages(),
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
