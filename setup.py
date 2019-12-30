from Cython.Build import cythonize, build_ext
from setuptools.extension import Extension
from setuptools import setup
# from distutils.core import setup

import os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
include_dirs = [dir_path + "/quicksectx", dir_path]


def get_version():
    """Load the version from version.py, without importing it.

    This function assumes that the last line in the file contains a variable defining the
    version string with single quotes.

    """
    try:
        with open('quicksectx/version.py', 'r') as f:
            return f.read().split('\n')[0].split('=')[-1].replace('\'', '').strip()
    except IOError:
        return "0.0.0a1"


extensions = [
    Extension(
        'quicksectx.quicksect1',
        sources=['quicksectx/quicksect1.pyx'],
        include_dirs=include_dirs,
    ),
    Extension(
        'quicksectx.quicksect2',
        sources=['quicksectx/quicksect2.pyx'],
        include_dirs=include_dirs,
    )
]

setup(name='quicksectx',
      version=get_version(),
      description="fast, simple interval intersection",
      long_description=open(Path(dir_path, 'README.rst').absolute()).read(),
      author="Brent Pedersen,Jianlin Shi",
      author_email="bpederse@gmail.com, jianlinshi.cn@gmail.com",
      url='https://github.com/jianlins/quickset',
      # cmdclass={'build_ext': Cython.Build.build_ext},
      package_dir={'quicksectx': 'quicksectx'},
      packages=['quicksectx'],
      ext_modules=cythonize(extensions, language_level=3),
      license='The MIT License',
      zip_safe=False,
      setup_requires=['cython>=0.24.1'],
      install_requires=['cython>=0.24.1'],
      test_suite='nose.collector',
      tests_require='nose',
      package_data={'': ['*.pyx', '*.pxd', '*.so', '*.dll']},
      )
