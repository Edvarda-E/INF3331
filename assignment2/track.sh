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
                    echo -e "\r\n" >> $LOGFILE
                fi
                currDateTime=`date "+%d/%m/%Y %H:%M:%S"`
                echo -e "START ${currDateTime}\r\nLABEL ${2}" | tee -a $LOGFILE
            fi
            ;;
        stop)
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                currDateTime=`date "+%d/%m/%Y %H:%M:%S"` 
                echo -e "END ${currDateTime}" | tee -a $LOGFILE
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
        log)
            while IFS='' read -r line || [[ -n $line ]]; do
                if [[ "${line}" =~ (START ){1}(.*) ]]; then
                    startTime="${line#* }"
                    removeNewline="${startTime/$'\r'/}"
                    startTimeConverted=`date -d "${removeNewline}" "+%T"`
                elif [[ "${line}" =~ (LABEL ){1}(.*) ]]; then
                    currentLabel="${line#* }"
                elif [[ "${line}" =~ (END ){1}(.*) ]]; then
                    endTime="${line#* }"
                    removeNewline="${endTime/$'\r'/}"
                    endTimeConverted=`date -d "${removeNewline}" "+%T"`

                    startTimeInSeconds=`date +%s -d ${startTimeConverted}`
                    endTimeInSeconds=`date +%s -d ${endTimeConverted}`
                    differenceInSeconds=`expr ${endTimeInSeconds} - ${startTimeInSeconds}`
                    finalTime=`date +%H:%M:%S -ud @${differenceInSeconds}`

                    echo "Task ${currentLabel}: ${finalTime}"
                fi
            done < $LOGFILE
            ;;
        *)
            echo "ERROR: track only accepts the parameters start, stop and status"
    esac
}