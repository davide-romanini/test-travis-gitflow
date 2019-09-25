from setuptools import setup, find_packages

setup(
    name='hello',
    use_scm_version=True,
    py_modules=(
        'hello',
    ),
    setup_requires=[
        "pytest-runner",
        "wheel",
        "setuptools_scm"
    ],
    tests_require=[
        "pytest"
    ]  
)

