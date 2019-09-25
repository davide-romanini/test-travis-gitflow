from setuptools import setup, find_packages

setup(
    name='hello',
    modules=(
        'hello',
    ),
    setup_requires=[
        "pytest-runner",
        "wheel"
    ],
    tests_require=[
        "pytest"
    ]  
)

