from os import path, pardir, chdir
from setuptools import setup, find_packages

README = open(path.join(path.dirname(__file__), 'README.rst')).read()
# allow setup.py to be run from any path
chdir(path.normpath(path.join(path.abspath(__file__), pardir)))

setup(
    name="django-onfido",
    version="0.12.1",
    packages=find_packages(),
    install_requires=[
        'django>=1.11',
        'psycopg2-binary>=2.6',
        'python-dateutil>=2.5',
        'requests>=2.10',
        'simplejson>=3.8',
        'django-mysql==2.3.0'
    ],
    include_package_data=True,
    description='Django app for integration with Onfido.',
    license='MIT',
    long_description=README,
    url='https://github.com/yunojuno/django-onfido',
    author='YunoJuno',
    author_email='code@yunojuno.com',
    maintainer='YunoJuno',
    maintainer_email='code@yunojuno.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
