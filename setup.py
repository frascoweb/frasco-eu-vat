from setuptools import setup


setup(
    name='frasco-eu-vat',
    version='0.3',
    url='http://github.com/frascoweb/frasco-eu-vat',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="EU VAT utilities for Frasco",
    py_modules=["frasco_eu_vat"],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'frasco',
        'frasco-models>=0.4',
        'suds',
        'requests'
    ]
)
