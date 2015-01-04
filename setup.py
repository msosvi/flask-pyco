from setuptools import setup

setup(name='Flask-Pyco',
    version='0.1',
    description='Simple flat file CMS inspired by Pico and Jekyll',
    url='http://github.com/mosvi/flask-pyco',
    author='Miguel Angel Sosvilla Luis',
    author_email='msosvi@enlosdetalles.net',
    license='BSD',
    packages=['flask_pyco'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask','mistune','PyYAML'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ])
