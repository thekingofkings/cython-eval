from distutils.core import setup

from Cython.Build import cythonize

setup(name='Tree traversal app',
      ext_modules=cythonize("pysrc_as_pyx/cnode.pyx"))

setup(name='Tree traversal app',
      ext_modules=cythonize("pysrc_static_typing/cnode.pyx"))

#setup(name='Tree traversal app',
#      ext_modules=cythonize("pynode.pyx"))
