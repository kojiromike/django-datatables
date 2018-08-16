import os
import sys
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

description = ''
if 'publish' in sys.argv:

    if 'test' in sys.argv:
        os.system('python setup.py sdist bdist_wheel upload -rtest')
    else:
        os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()


if 'upload' in sys.argv:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')


with open('LICENSE') as f:
    license = f.read()

setup(
    name='django-datatables',
    version='0.1.1',
    description='Django and Datatables made easy.',
    url='https://github.com/scuml/django-datatables',

    license=license,
    long_description=description,
    author='Stephen Mitchell, Patrick Coronel',
    author_email='stephen@echodot.com',

    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={'': ['LICENSE']},

    install_requires=[
        'django>=2',
    ],
    include_package_data=True,
    zip_safe=False,                 # because we're including static files
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)
