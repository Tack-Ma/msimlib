from setuptools import setup

install_requires = [
    'numpy'
]

packages = [
    'msimlib',

]

console_scripts = [
    # 'sample_lib_cli=sample_lib_cli.call:main',
]


setup(
    name='msimlib',
    version='0.0.0',
    packages=packages,
    install_requires=install_requires,
    entry_points={'console_scripts': console_scripts},
)