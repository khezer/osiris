import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_layout',
    'waitress',
    'cornice',
    'pymongo',
    'colander',
    'Babel',
    'lingua',
]

devtools_requires = [
    'pyramid_debugtoolbar',
    'pyramid_bpython',
]

tests_requires = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(
    name='osiris',
    version='0.0',
    description='osiris',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_requires,
        'devtools': devtools_requires
    },
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = osiris:main
    [pyramid.scaffold]
    osirisproject=osiris.scaffolds:OsirisProjectTemplate
    osirisapp=osiris.scaffolds:OsirisAppTemplate
    """,
)
