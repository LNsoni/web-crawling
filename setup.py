from setuptools import setup, find_packages

setup(
    name='mu_crawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'crawl4ai'
    ],
    entry_points={
        'console_scripts': [
            'mycrawler=app.entry:main',
        ],
    },
)