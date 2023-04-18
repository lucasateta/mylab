from setuptools import setup, find_packages

setup(
    name='XYZThings',
    version='0.1.0',
    discription='XYZThings',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "orjson",
        "email_validator",
        "pyee",
        "jsonschema",
        "ifaddr",
        "loguru",
        "zeroconf",
        "mkdocs-material",
        "async-cron",
        "gmqtt",
        "tinydb",
    ],
    extra_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "httpx",
            "flake8",
            "pytest",
            "black",
        ]
    },
)
