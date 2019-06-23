from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import sys
import os

libs = os.popen('ldconfig -p | grep libopencv')
libs = libs.readlines()
lib_paths = [l.split('=>')[-1].strip('\n').strip(' ') for l in libs]

# Find opencv libraries in lib_folder
cvlibs = list()
lib_folders = set()
for file in lib_paths:
    file_split = file.split('.')
    cvlibs.append(file_split[0])
    lib_folders.add(file.split('libopencv')[0])
lib_folders = list(lib_folders)
cvlibs = list(set(cvlibs))
cvlibs = ['-L{}'.format(lib_folder) for lib_folder in lib_folders] + \
         ['opencv_{}'.format(lib.split(os.path.sep)[-1].split('libopencv_')[-1]) for lib in cvlibs]

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(Extension("opencv_mat",
                                    sources=["opencv_mat.pyx", "globalmatting.cpp", "guidedfilter.cpp"],
                                    language="c++",
                                    include_dirs=[numpy.get_include(),
                                                  os.path.join('/usr', 'include', 'opencv2'),
                                                 ],
                                    library_dirs=lib_folders,
                                    libraries=cvlibs,
                                    )
                          )
)
