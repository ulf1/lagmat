from setuptools import setup
import pypandoc


setup(name='lagmat',
      version='0.3.0',
      description=(
          "Lagmatrix. Create array with time-lagged copies of the features"),
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/lagmat',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['lagmat'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.*'],
      python_requires='>=3.6',
      zip_safe=False)
