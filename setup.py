# to run: python setup.py install
try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup
#from distutils.extension import Extension

setup(name="gaiascanlaw",
      version='0.2.0',
      description='gaia scan law',
      author='Zephyr Penoyre',
      author_email='zephyrpenoyre@gmail.com',
      url='https://github.com/zpenoyre/gaiascanlaw',
      license='GNU GPLv3',
      packages=find_packages(),
      install_requires=['numpy','astropy','scipy','healpy'],
      include_package_data=True,
      package_data={'': ['data/*.fits']},
      long_description='https://astrometpy.readthedocs.io/en/latest/index.html'
      )
