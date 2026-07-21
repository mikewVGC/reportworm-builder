from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="reportworm-builder",
    version="0.1",
    include_package_data=True,
    python_requires='>=3.9',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="Mike Watson",
    author_email="mike.watson@gmail.com",
    description="Site builder for Reportworm and Reportworm-adjacent projects",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: BSD License",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)
