from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

setup(
    name='opposite-day',
    version='1.0.0',
    description='It is Opposite Day Now',
    url='https://github.com/yuvipanda/opposite-day',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='3 Clause BSD',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)
