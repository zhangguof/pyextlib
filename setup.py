from distutils.core import setup, Extension
from Cython.Build import cythonize

objs = []

inc_dirs = ['.']
sources = []

libs = []
lib_dirs = ['.']


def do_setup(args):
    pymod = Extension('pylib',
                      # define_macros = [('MAJOR_VERSION', '1'),
                      #                  ('MINOR_VERSION', '0')],
                      include_dirs=inc_dirs,
                      libraries=libs,
                      library_dirs=['.'],
                      extra_objects=objs,  # or ['alib.obj'],
                      sources=sources,  # or ['clib.c', 'pylib.c']
                      )
    setup(name='pylib',
          version='1.0',
          description='This is a demo package',
          author='TonyZhang',
          long_description = '''
                This is really just a demo package.
                ''',
          script_args=args,
          ext_modules=[pymod])


if __name__ == "__main__":
    import sys
    do_setup(sys.argv[1:])
