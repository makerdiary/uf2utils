import setuptools

DISTRIBUTION_NAME = 'uf2conv'

setuptools.setup(
    name=DISTRIBUTION_NAME,
    version='0.0.1',
    description='Packing and unpacking UF2 files.',
    author='Makerdiary',
    url='https://github.com/makerdiary/uf2utils',
    python_requires='>=3.6',
    include_package_data=True,
    packages=['uf2conv'],
    package_data={
        'uf2conv': ['uf2families.json']
    },
    entry_points={
        'console_scripts': ['uf2conv = uf2conv.uf2conv:main']
    }
)
