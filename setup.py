from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

setup(name='Tree traversal cython compiling pysrc',
      ext_modules=cythonize("pysrc_as_pyx/cnode.pyx"))

setup(name='Tree traversal cython static typing',
      ext_modules=cythonize("pysrc_static_typing/cnode.pyx"))

extensions = [Extension("clib_node.pynode", sources=["clib_node/pynode.pyx"], include_dirs=["clib_node"],
                        extra_compile_args=["-g"], extra_link_args=["-g"])]
setup(name='Tree traversal C lib',
      ext_modules=cythonize(extensions))
