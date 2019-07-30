from setuptools import setup, find_packages

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(name='judoisoftpy',
      version='0.1.0',
      author='Tobias Hoff',
      author_email='tobias@die-hoffs.net',
      url='https://github.com/ToSa27/judoisoftpy',
      description='Python client for the Judo i-Soft Plus API',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests'],
      extras_require={
            'testing': ['nose',],
      },
    )