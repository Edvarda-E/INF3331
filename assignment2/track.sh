#!/bin/bash -x

function track () {
    action=$1
    lastLineOfFile=$(tail -1 "$LOGFILE")
    case "$action" in
        start)
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                echo "ERROR: Another task is already running. Run track stop to end it."
            elif [ "$#" -le "1" ]; then
                echo "ERROR: Please provide a label as follows: track start \"label\""
            else
                if [[ "${lastLineOfFile}" =~ (END ){1}(.*) ]]; then
                    echo -e "\r\n\r\n" >> $LOGFILE
                fi
                currDateTime=`date +"%c"`
                echo -e "START ${currDateTime}\r\nLABEL ${2}" | tee -a $LOGFILE
            fi
            ;;
        stop)
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                currDateTime=`date +"%c"` 
                echo -e "\r\nEND ${currDateTime}" | tee -a $LOGFILE
            else
                echo "ERROR: No task is currently active"
            fi
            ;;
        status)
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                echo "Your current task is ${lastLineOfFile#* }"
            else
                echo "ERROR: No task is currently active"
            fi
            ;;
        *)
            echo "ERROR: track only accepts the parameters start, stop and status"
    esac
}