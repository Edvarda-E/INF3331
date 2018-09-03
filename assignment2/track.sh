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
                    startTimeConverted="$(convertLineFromFileToTime "${line}")"
                elif [[ "${line}" =~ (LABEL ){1}(.*) ]]; then
                    currentLabel="${line#* }"
                elif [[ "${line}" =~ (END ){1}(.*) ]]; then
                    endTimeConverted="$(convertLineFromFileToTime "${line}")"
                    
                    calculateAndPrintLog $startTimeConverted $endTimeConverted
                fi
            done < $LOGFILE
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                currTime=`date "+%H:%M:%S"`
                calculateAndPrintLog $startTimeConverted $currDateTime
            fi
            ;;
        *)
            echo "ERROR: track only accepts the parameters start, stop and status"
    esac
}

calculateAndPrintLog () {
    startTimeInSeconds=`date +%s -d ${1}`
    endTimeInSeconds=`date +%s -d ${2}`
    differenceInSeconds=`expr ${endTimeInSeconds} - ${startTimeInSeconds}`
    finalTime=`date +%H:%M:%S -ud @${differenceInSeconds}`

    echo "${currentLabel}: ${finalTime}"
}

convertLineFromFileToTime () {
    lineToBeConverted="$1"
    removeHelpTextFromLine="${lineToBeConverted#* }"
    removeNewlineFromEndOfLine="${removeHelpTextFromLine/$'\r'/}"
    convertFromDateTimeFormatToOnlyTime=`date -d "${removeNewlineFromEndOfLine}" "+%T"`
    echo "$convertFromDateTimeFormatToOnlyTime"
}