import setuptools

setuptools.setup(
    name='ixc-django-storages',
    use_scm_version={'version_scheme': 'post-release'},
    py_modules=['ixc_storages'],
    install_requires=[
        'django-storages',
    ],
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/ixc-django-storages',
    license='BSD',
)
