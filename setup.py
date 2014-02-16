from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='aaargh',
    version='0.6',
    description='An astonishingly awesome application argument helper',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Wouter Bolsterlee',
    author_email='uws@xs4all.nl',
    url='https://github.com/wbolster/aaargh',
    packages=find_packages(),
    license='BSD',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
    ),
)
