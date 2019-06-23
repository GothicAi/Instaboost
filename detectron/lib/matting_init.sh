#!/usr/bin/env bash
if [ $# -gt 0 ]
then
    py_path=`which $1`
else
    py_path=`which python3 || which python`
fi

py_ver=`${py_path} -c "import sys; print(sys.version_info.major)"`

if [ ${py_ver} -eq 2 ]
then
    echo "Python3 is required but not found."
    exit 1
fi

cd AugSeg/global_matting && echo "building global_matting module.."
echo $py_path
$py_path setup.py build_ext --inplace && \
 echo "performing test.." && ${py_path} test.py && \
 echo 'done'
