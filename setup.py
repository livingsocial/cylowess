'''
Setup file for cylowess.pyx, a faster lowess smoother in Cython.
'''
try:
    from distutils.core import setup
    from distutils.extension import Extension
    from Cython.Distutils import build_ext
    import numpy as np

    setup(
        name='cylowess',
        cmdclass = {'build_ext' : build_ext},
        include_dirs = [np.get_include()],
        ext_modules = [Extension('cylowess', ['cylowess.pyx'])]
        )
except:
    pass
