from pathlib import Path
from setuptools import setup
from setuptools import find_packages

from pip.req import parse_requirements
from pip.download import PipSession


def requirements(filename):
    """Parse requirements from requirements.txt."""
    path = str(Path(filename))
    reqs = parse_requirements(path, session=PipSession())
    return [str(req.req) for req in reqs]


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
    test_require=requirements('requirements-dev.txt'),
    # install_requires=Path('requirements.in').read_text().split('\n'),

    include_package_data=True,
    zip_safe=False
)
