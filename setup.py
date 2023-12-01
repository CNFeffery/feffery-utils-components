import json
import os
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    author_email=package['email'],
    packages=[package_name],
    include_package_data=True,
    package_data={
        'feffery_antd_components': ['*']
    },
    license=package['license'],
    description=package.get('description', package_name),
    install_requires=[
        'dash>=2.10.2'
    ],
    classifiers=[
        'Framework :: Dash',
    ],
    homepage='https://github.com/CNFeffery/feffery-utils-components',
    url='https://github.com/CNFeffery/feffery-utils-components'
)
