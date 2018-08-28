#!/bin/bash -x

function track () {
    action=$1
    case "$action" in
        start)
            echo "Start passed"
            ;;
        stop)
            echo "Stop passed"
            ;;
        status)
            echo "Status passed"
            ;;
        *)
            echo "ERROR: track only accepts the parameters start, stop and status"
    esac
}