from setuptools import setup

setup(name='pylation',
      version='0.1',
      description='Test upload of relational network',
      url='http://github.com/bheff88/pylation',
      author='Braden Heffernan',
      author_email='baheffer@ucalgary.ca',
      license='MIT',
      packages=['pylation'],
      install_requires=['keras-gpu'],
      zip_safe=False)