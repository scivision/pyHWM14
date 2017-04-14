#!/usr/bin/env python
import setuptools
from glob import glob
from os.path import join
from numpy.distutils.core import Extension, setup

req = ['nose','numpy','matplotlib','pathlib2',
       'timeutil']

name = 'pyhwm2014'

ext = Extension( extra_compile_args=['-w'],
            extra_f90_compile_args=['-w'],
            f2py_options=[ '--quiet' ],
            name='hwm14',
            sources=[ 'source/hwm14.f90']
             )

hwmData1 = glob(join('data', '*.dat'))
hwmData2 = glob(join('data', '*.bin'))
hwmDataFiles = [(join(name, 'data'), hwmData1),
                (join(name, 'data'), hwmData2)]

setup( author=['Ronald Ilma','Michael Hirsch, Ph.D'],
        data_files=hwmDataFiles,
        description='HWM14 neutral winds model',
        ext_modules=[ ext ],
        ext_package=name,
        name=name,
        packages=[name],
        url='https://github.com/rilma/pyHWM14',
        version='1.1',
        install_requires=req,
        dependency_links=[
      'https://github.com/rilma/TimeUtilities/zipball/master#egg=timeutil'],
        classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          ],
)
