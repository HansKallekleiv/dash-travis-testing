from setuptools import setup, find_packages


tests_require = [
    'chromedriver-binary>=74.0.3729.6.0',
    'ipdb',
    'percy',
    'selenium>=3.141.0',
    'flake8',
    'pylint',
    'pytest-dash>=2.1.2',
    'mock'
]

setup(
    name='dash-travis-testing',
    description='Testing things',
    long_description='Testing things',
    long_description_content_type='text/markdown',
    url='https://github.com/hanskallekleiv/dash-travis-testing',
    author='HK',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'dash==2.15.0'
    ],
    tests_require=tests_require,
    extras_require={'tests': tests_require},
)
