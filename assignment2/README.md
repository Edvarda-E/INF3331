# Assignment 2
This is the directory for assignment 2 done by Edvarda Eriksen (ererikse).

## Task 2.1 - Climbing the directory tree
To run the script, make it executable and source the file as follows
```
$ chmod a+x climb.sh
$ . ./climb.sh
# or
$ source climb.sh
```
or [add it to your .bashrc](https://unix.stackexchange.com/a/106606)

As the task demands
* `climb` and `climb 1` is interpreted the same way
* `climb` and `climb 1` is equivalent to `cd ..`
* `climb 5` is equivalent to `cd ../../../../../`

**Additional decisions**
* If more than one positional parameter is passed to the script, e.g. `climb 1 2`, the script will echo an error message and return.
* The script is verbose, meaning that it will echo what is does to the terminal, e.g. `Walking up one directory`.

## Task 2.2 - A simple time tracker
*Before* you run the script, remember to set an environmental variable called `$LOGFILE` with an assigned `.txt` file, so that the script runs correctly. However, if you should forget, the script will print an error informing you on how to proceed.

To run the script, make the script executable and then source it
``` 
$ chmod a+x track.sh
$ . ./track.sh
$ track start "Task 1"
...
```
All functionality requested in the task is covered

**Additional decisions**
* I have slightly changed the format of the output, so expected output is for example:
```
START 03/09/2018 15:38:49
LABEL Task 1
END 03/09/2018 15:38:53
```

**Known issues**
* If you run the start action directly using e.g. `bash track.sh start`, the script will not warn you that it does not accept this action without the label.
* I have solved the task with respects to LF lineendings, so that it works in the terminal and on Linux. Due to the different nature of line endings between the Windows OS and Linux, if you open the log.txt in Windows it will look a bit odd.

## Task 2.3 - Make the tracker useful
This task is implemented in the same script as task 2.2, and can be run (after the script is executable and sourced) as follows:
```
$ track log
```

It will produce its output only in the terminal, not in a logfile, as the format `<LABEL>: <TIME SPENT>`. Example output can look like:
```
$ track log
Walking the dog: 01:50:51
Cleaning: 05:00:07
Time spent at work: 07:03:17
Task 4: 03:40:13
Task 5: 07:44:53
Task 6: 00:20:54
```

Testing data is available in `./log.txt`

**Additional decisions**
* If the logfile is empty when you run `track log`, the script will return with exit code 1, providing a warning stating so.
* If a task is currently running during logging, it will take a snapshot of the current time and print the time from the task started up until now.
* The log function *does not* support tasks that span over several days, as this was not required in the task.
* As it doesn't support tasks that span over several days, it does not verify whether the end time is smaller than start time either.