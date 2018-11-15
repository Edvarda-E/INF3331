# Assignment 4
This is the directory for assignment 4, done by Edvarda Eriksen (ererikse) who is enrolled in INF4331.

## General notice
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
* All images are stored under `~/imgs/temp/`
* Files will be generated in the name format `<month>_plot.png`, and hence overwrite each other by month to keep folder
 size down and to easily be able to identify what image was just created


For `plot_CO2()`:
* All images are stored under `~/imgs/co2/`
* * Files will be generated in the name format `CO2_leves_<start_year>_<end_year>.png`, and hence overwrite each other 
if the same year ranges are run twice. Again this to keep folder size down and to easily be able to identify what image
 was just created


## 6.2 - Web App for Visualisation