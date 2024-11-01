from setuptools import find_packages, setup

setup(
    name="dagster_snowflake_project_1",
    packages=find_packages(exclude=["dagster_snowflake_project_1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
