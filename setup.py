from setuptools import setup

setup(
    name="JobsSearch App",
    version="1.03072016",
    description="Searching public job sites and displaying real time data. ",
    author="Catalin",
    author_email="bota.catalin@gmail.com",
    packages=["jobs", "jobs.model", "jobs.services", "jobs.ui", "jobs.tests"],
    requires=['lxml','requests']
)

