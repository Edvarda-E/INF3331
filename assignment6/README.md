# Assignment 6
This is the directory for assignment 6, done by Edvarda Eriksen (ererikse) who is enrolled in INF4331.

## General notice
This assignment was solved on a Ubuntu 17 system and requires the following packages:
- Python 3 or above
- Numpy
- Pandas
- Flask

In `temperature_CO2_plotter.py` from exercise 6.1 the modules `plot_temperature()` and `plot_CO2()` do have quite
similar code due to the tasks being quite similar, however I found my attempt to abstract out the similar parts to be
too difficult to read as it would be riddled with if-statements, and hence I found it better to leave it as is. 
## 6.1 - Plotter for temperature and CO2 values
Running the script
```
$ python3 temperature_CO2_plotter.py temperature 2000 2012 18 22 -month August

$ python3 temperature_CO2_plotter.py co2 1800 2012 0 12000
``` 
As always you can use `python3 temperature_CO2_plotter.py -h` for help on what values the argparses expects. There
should be sufficient testing so that if you make a mistake the program will let you know. See the 
`verify_positional_parameters()` module for positional parameters tests.


I made the assumption that when speaking of time range in temperature, we are supposed to display the data for the 
given month over the given years. Example: If you pass the time range 2000 to 2012 and August, it will plot the data for
 August for each year from 2000 to 2012.

**Additional decisions**

For both:
* I have made the year ranges and the y-values as positional parameters required.
* The year values must be different by atleast 1, e.g. you can't put `2012 2012` and receive data for only 2012.
* The script will warn you if the y-values are entirely outside of the data set (e.g. ymin is larger than the highest 
value), however it will still save the image as it isn't strictly an error.
* I have let DataFrame handle the tick rate, as this makes nicer, less dense graphs. The drawbacks are that it also 
makes the graphs less detailed and it turns the year values into decimal values if the years are very close, e.g. 
2011-2012 will turn into 2011.0, 2011.2 etc.


For `plot_temperature()`:
* All images are stored under `~/static/images/temp/`
* Files will be generated in the name format `<month>_plot.png`, and hence overwrite each other by month to keep folder
 size down and to easily be able to identify what image was just created


For `plot_CO2()`:
* All images are stored under `~/static/images/co2/`
* * Files will be generated in the name format `CO2_levels_<start_year>_<end_year>.png`, and hence overwrite each other 
if the same year ranges are run twice. Again this to keep folder size down and to easily be able to identify what image
 was just created


## 6.2 & 6.3 - Web App for Visualisation
Running the webapp:
```
$ export FLASK_APP=web_visualization.py
$ export FLASK_ENV=development
$ flask run
```

The FLASK_ENV is optional but nice to have, as it will include code changes in refreshes of the webpage.

When you first open the application you are met with a frontpage, containing radio buttons and a form. If you change 
the radiobutton the forms will be changed out with the form needed for the respective implementation (warning: this 
requires JavaScript). Once you have chosen your implementation and the desired values you will be taken to a new website
where the desired plot and the data you put in will be displayed. Then you can go back "home" and start again.

**Additional decisions**
* I didn't have the time to properly implement input validation on the frontend side, so the user is advised to only 
choose end year input values that are smaller than the start year. Same goes for y-values. If you run into issues I 
suggest running the implementation and the desired values from the terminal, as most cases are covered by the python
script.

## 6.4 - CO2 by Country
Running the script:
```
$ python3 temperature_CO2_plotter.py co2_by_country 2000 15
```
or use the webapp as described above.

This was one braintwister of a graph to make, due to the far too big list of countries. In the end I decided to make a 
looooong y-axis with the values only barely not overlapping. This was a product of trial-and-error with figsizes, so I
cannot gurantee a beautiful output on all monitors.

In addition I ended up interpreting the task as asking for a *single* threshold, where I have emphasised what graphs 
that lie above/below the threshold with a blue and red color. To further show where the threshold is I added a vertical 
line spanning across the graph. See examples under 'images/co2_by_country/'. This approach was inspired by 
[this StackOverflow answer](https://stackoverflow.com/a/28129801).

Furthermore, I decided that due to the size of the dataset I would make the user choose only one year, although this is
not specified in the task, as including all the years would just make the graph unreadable/unmanageable. 

**Reflection**
- When it came to handling the three argparsers I ended up importing sys and handling the argparser for CO2 by Country
separately. This is by no means an elegant approach and I realise that perhaps it would have been a better decision to
use subparsers, however I am satisfied with my solution.

## 6.5 - Documentation
I solved this exercise using pydoc. The documentation is called `temperature_CO2_plotter.html` and can be found in the
 `~/templates` folder. It was generated as follows:
```
$ pydoc -w temperature_CO2_plotter
```
and then manually moved into the `~/templates` folder in order to be picked up by Flask.