#!/bin/bash -x

function climb () {
    if [ "$#" -ge "2" ]; then
        echo "ERROR: This function can only handle one positional parameter"
        return 1
    fi

    ARG1=${1:-1}
    if [ "$ARG1" == "1" ]; then
        echo "Walking up one directory"
        cd ..
    else
        foo="cd "
        for (( i=0; i<$1; i++ ))
            do
                foo+="../"
            done
        echo "Walking up ${ARG1} directories"
        $foo
    fi
}