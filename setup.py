from pathlib import Path
from setuptools import setup
from setuptools import find_packages


setup(
    name='tailor',

    version=Path('VERSION').read_text().strip(),

    description='Tailor',
    long_description=Path('README.md').read_text(),

    author='Alejandro Castaño Gonzalez',
    author_email='unocongafas@gmail.com',

    url='https://bitbucket.org/unocongafas',
    download_url='https://bitbucket.org/unocongafas',

    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    package_dir={'': 'src'},
    packages=find_packages('src'),

    setup_requires=['pytest-runner'],
    # install_requires=Path('requirements.in').read_text().split('\n'),

    include_package_data=True,
    zip_safe=False
)
