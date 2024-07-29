from setuptools import setup, find_packages

setup(
    name='consume_github_api',
    version='0.1',
    author='Thabiso Mokgete',
    author_email='thabiso.mokgete@umuzi.org',
    description='A script to consume the GitHub API to fetch pull requests from a specified repository within a given date range.',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'consume-github-api=src.consume_github_api:main',
        ],
    },
)
