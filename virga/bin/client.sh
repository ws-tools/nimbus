#!/bin/bash

dir=`dirname $0`
cd $dir/..
pypath=`pwd`
if [ "X${PYTHONPATH}" == "X" ]; then
    export PYTHONPATH=$pypath
else
    export PYTHONPATH=$pypath:${PYTHONPATH}
fi

exec python ./pyvirga/client.py "${@}"
