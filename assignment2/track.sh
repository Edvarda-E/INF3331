#!/bin/bash -x

function track () {
    action=$1
    if [[ -z $LOGFILE ]]; then
        echo "Please create an environmental variable called \$LOGFILE"
        return 1
    fi
    lastLineOfFile=$(tail -1 "$LOGFILE")
    case "$action" in
        start)
            # The RegEx used throughout this program checks wheter the line
            # starts with whatever is within ([...]), here 'LABEL '
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                echo "ERROR: Another task is already running. Run track stop to end it."
            elif [ "$#" -le "1" ]; then
                echo "ERROR: Please provide a label as follows: track start \"label\""
            else
                # If the last line of the file is END, add whitespace
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
                # '#* ' is substring removal up until the first space, removing 
                # LABEL from the string
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

            # If a task is currently active, we take a snapshot of the current
            # time to see how long it's been since the task has started
            if [[ "${lastLineOfFile}" =~ (LABEL ){1}(.*) ]]; then
                currTime=`date "+%H:%M:%S"`
                calculateAndPrintLog $startTimeConverted $currDateTime
            fi
            ;;
        *)
            echo "ERROR: track only accepts the parameters start, stop and status"
    esac
}

# Helper function that calculates and prints the timedifference of two timestamps
calculateAndPrintLog () {
    # Convert from 'H:M:S' to only seconds
    startTimeInSeconds=`date +%s -d ${1}`
    endTimeInSeconds=`date +%s -d ${2}`
   
    differenceInSeconds=`expr ${endTimeInSeconds} - ${startTimeInSeconds}`
    # Converts the difference back to 'H:M:S' format
    finalTime=`date +%H:%M:%S -ud @${differenceInSeconds}`

    echo "${currentLabel}: ${finalTime}"
}

# Converts log input to only date format
convertLineFromFileToTime () {
    lineToBeConverted="$1"
    removeHelpTextFromLine="${lineToBeConverted#* }" # Removes START, LABEL..
    removeNewlineFromEndOfLine="${removeHelpTextFromLine/$'\r'/}"
    convertFromDateTimeFormatToOnlyTime=`date -d "${removeNewlineFromEndOfLine}" "+%T"`
    echo "$convertFromDateTimeFormatToOnlyTime"
}