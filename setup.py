"""
Flask-MongoEngine
--------------

Flask support for MongoDB using MongoEngine.
Includes `WTForms`_ support.

Links
`````

* `development version
  <https://github.com/sbook/flask-mongoengine/raw/master#egg=Flask-MongoEngine-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-MongoEngine',
    version='0.1.2-dev',
    url='https://github.com/sbook/flask-mongoengine',
    license='BSD',
    author='Ross Lawley',
    author_email='ross.lawley@streetlife.com',
    description='Flask support for MongoDB and with WTF model forms',
    long_description=__doc__,
    packages=['flask_mongoengine',
              'flask_mongoengine.wtf'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'mongoengine',
        'flask-wtf'
    ],
    include_package_data=True,
    tests_require=[
        'nose',
        'flask-debugtoolbar'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
