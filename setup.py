from setuptools import setup

setup(
    name='xrecon',
    version='1.0.0',
    description='Fast and modular web reconnaissance and endpoint discovery tool.',
    author='Amel Žiga',
    py_modules=['xrecon'],
    install_requires=[
        'requests', 'beautifulsoup4' ,'tldextract' 
    ],
    entry_points={
        'console_scripts': [
            'xrecon = xrecon:main'
        ],
    },
)
