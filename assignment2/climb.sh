#!/bin/bash

function climb () {
    # If more than one positional parameter is passed, the function will return
    # with an error code
    if [ "$#" -ge "2" ]; then
        echo "ERROR: This function can only handle one positional parameter"
        return 1
    fi

    # Sets ARG1 to be $1, with the default value of 1 if $1 is unset or null
    ARG1=${1:-1}
    if [ "$ARG1" == "1" ]; then
        echo "Walking up one directory"
        cd ..
    else
        walkPath="cd "
        for (( i=0; i<$ARG1; i++ ))
            do
                walkPath+="../"
            done
        echo "Walking up ${ARG1} directories"
        $walkPath
    fi
}