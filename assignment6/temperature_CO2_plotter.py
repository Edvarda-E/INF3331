import sys
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np


def plot_temperature(year_range, ymin, ymax, month):
    """"
    Module that generates a plot within the provided time- and temperature range (y-values), based on the temperature
    data set temperature.csv found in the data directory.

    Arguments:
        year_range (tuple): Start and end year for the plot
        ymin (float): Smallest value for the temperature, meaning the y-axis
        ymax (float): Largest value for the temperature, meaning the y-axis
        month (str): What month to display temperature data for

    Returns:
        Saves the plot with the given boundaries as an image, in the ./static/images/temp directory
    """
    temp = ""

    try:
        # Use pandas to read the csv file, separating values on ,
        temp = pd.read_csv('data/temperature.csv', sep=",")

        # Here I use boolean indexing to extract the parts of the dataframe within the year range only
        extracted_data_by_year = temp[(temp['Year'] >= year_range[0]) & (temp['Year'] <= year_range[1])]

        lowest_temp_value = 0
        highest_temp_value = 0
        # Warns the user if the y-values are completely outside of the data set
        if month != "All":
            lowest_temp_value = extracted_data_by_year[month].min()
            highest_temp_value = extracted_data_by_year[month].max()
        else: # Month = "All"
            #Finds the max and min value of entire dataset
            #First max() returns a series with max for each column, second max() finds the max-value in series
            lowest_temp_value = extracted_data_by_year.iloc[:, 2:].min(1).min()
            highest_temp_value = extracted_data_by_year.iloc[:, 2:].max(1).max()

        if ymax < lowest_temp_value:
            print("WARNING: Your ymax value is less than the lowest temperature value in the data set for " + month)
            print("The lowest temperature is " + str(lowest_temp_value) + " while you provided the ymax " + str(ymax))
        elif ymin > highest_temp_value:
            print("WARNING: Your ymin value is higher than the highest temperature value in the data set for " + month)
            print("The highest temperature is " + str(highest_temp_value) + " while you provided the ymin " + str(ymin))

        if month == "All":
            plot = extracted_data_by_year.plot(
                title="Temperature Plot",
                x='Year',                   # Sets the x-axis to be years
                #y=month,                    # Sets the y-axis to be the temperature for the desired month
                ylim=(ymin, ymax),          # ylim=(bottom_value, top_value)
                grid=True)
        else:
            plot = extracted_data_by_year.plot(
                title="Temperature Plot",
                x='Year',                   # Sets the x-axis to be years
                y=month,                    # Sets the y-axis to be the temperature for the desired month
                ylim=(ymin, ymax),          # ylim=(bottom_value, top_value)
                grid=True)

        plot.set_xlabel('Year temperature was measured')
        plot.set_ylabel('Temperature in Degrees Celsius')
        plot.grid(linestyle="dotted")
        # plot is a DataFrame AxesSubplot and has no savefig() module, hence I have to use the pyplot plt module instead
        plt.savefig('static/images/temp/{}_plot.png'.format(month))
        #plt.show()

    except FileNotFoundError as e:
        print("Couldn't find the temperature data set")


def plot_CO2(year_range, ymin, ymax):
    """
    Module that generates a plot within the provided time- and CO2 emission range (y-values), based on the CO2 data set
    CO2.csv found in the data directory.

    Arguments:
        year_range (tuple): Start and end year for plot
        ymin (int): Smallest value for the y-axis
        ymax (int): Largest value for the y-axis

    Returns:
        Saves the plot with the given boundaries as an image, in the ./static/images/co2 directory
    """

    co2_data = ""
    try:
        # Use pandas to read the csv file, separating values on ,
        co2_data = pd.read_csv('data/CO2.csv', sep=',')

        # Again I use boolean indexing to extract the parts of the dataframe within the year range only
        extracted_data_by_year = co2_data[(co2_data['Year'] >= year_range[0]) & (co2_data['Year'] <= year_range[1])]

        # Warns the user if the y-values are completely outside of the data set
        lowest_co2_value = extracted_data_by_year['Carbon'].min()
        highest_co2_value = extracted_data_by_year['Carbon'].max()

        if ymax < lowest_co2_value:
            print("WARNING: Your ymax value is less than the lowest CO2 value in the data set within the year range")
            print("The lowest CO2 value is " + str(lowest_co2_value) + " while you provided the ymax " + str(ymax))
        elif ymin > highest_co2_value:
            print("WARNING: Your ymin value is larger than the highest CO2 value in the data set within the year range")
            print("The highest CO2 value is " + str(highest_co2_value) + " while you provided the ymin " + str(ymin))

        plot = extracted_data_by_year.plot(
            title="CO2 Plot",
            x='Year',
            y='Carbon',
            ylim=(ymin, ymax),
            grid=True
        )
        plot.set_xlabel('Year CO2 was measured')
        plot.set_ylabel('CO2 level')
        plot.grid(linestyle="dotted")
        plt.savefig("static/images/co2/CO2_levels_{}_{}".format(str(year_range[0]), str(year_range[1])))
        # plt.show()
    except FileNotFoundError as e:
        print("Couldn't find the temperature data set")



def plot_CO2_by_country(year, threshold):
    """
    Module that generates a plot for the given year and adds split the  CO2 emissions based on the provided threhsold,
    where the data is retireved  from the CO2_by_country.csv data set found in the data directory.
    CO2.csv found in the data directory.

    Arguments:
        year (int): What year to plot CO2 emissions for
        threshold (float): The upper/lower threshold for the CO2 emission

    Returns:
        Saves the plot with the given boundaries as an image, in the ./static/images/co2_by_country directory
    """

    co2_data = ""

    try:
        co2_data = pd.read_csv('data/CO2_by_country.csv', sep=",")

        # I had some issues with the year being interpreted as an integer
        year = str(year)
        y_pos = np.arange(len(co2_data[year]))          # For the yticks
        countries = co2_data['Country Name'].values
        emissions = co2_data[year].values

        # Separates the emissions based on the threshold, with values above and below
        above_threshold = np.maximum(emissions - threshold, 0)
        below_threshold = np.minimum(emissions, threshold)

        # pyplot doesn't like arrays without commas, so I convert them to lists to add commas between the values
        above_threshold_with_commas = list(above_threshold)
        below_threshold_with_commas = list(below_threshold)

        fig, ax = plt.subplots(figsize=(10, 30))
        ax.barh(y_pos, below_threshold_with_commas, color="b")
        ax.barh(y_pos, above_threshold_with_commas, color="r", left=below_threshold)
        plt.yticks(y_pos, countries)
        plt.gca().invert_yaxis()        # Invert the y-axis so the countries appear in alphabetical order
        plt.axvline(threshold,          # Generates the threshold vertical line through the plot
                    color='k',
                    linestyle='dashed',
                    label="Threshold")
        plt.grid(linestyle="dotted")

        plt.title("CO2 Emission by Country for Year {}".format(year))
        plt.xlabel('CO2 Emission per Metric Capita')
        plt.tight_layout()              # Ensures all the country names make it into the picture
        plt.legend()                    # Display labels for the threshold
        plt.savefig(fname="static/images/co2_by_country/CO2_levels_{}".format(year),
                                dpi=80)

        # Store a dpi to prevent the result being too different on different monitors
    except FileNotFoundError as e:
        print("Couldn't find the file")

def verify_positional_parameters(temp_args, parser):
    """
    Checks that the positional parameters have the correct values for the given data set

    Arguments:
        temp_args: an argparse object containing the given parameters
        parser: an ArgumentParser object with the added args
    Returns:
        Parser errors if applicable
    """
    data = temp_args.data
    start_year = temp_args.time_range_start
    end_year = temp_args.time_range_end

    # Verifications needed regardless of data set
    if start_year > end_year:
        parser.error("The start year (time_range_start) must be before the end year (time_range_end)!")
    if start_year == end_year:
        parser.error("Must be atleast one year difference between the year ranges, e.g. 2011 2012")
    if temp_args.ymin > temp_args.ymax:
        parser.error("The ymin value must be smaller than the ymax value")
    if temp_args.ymin == temp_args.ymax:
        parser.error("ymin and ymax cannot be the same value")

    # Data set specific verifications
    if data == "temperature":
        if temp_args.month is None:
            parser.error("Temperature requires a given month, run with -h for help")
        # Hardcoded year range values from the temperature dataset
        elif start_year < 1816 or start_year > 2012:
            parser.error("time_range_start must be within the interval 1816 to 2012 for temperature")
        elif end_year < 1816 or end_year > 2012:
            print("Hello")
            parser.error("time_range_end must be within the interval 1816 to 2012 for temperature")
        else:
            return
    else:  # co2 is the data
        # Hardcoded year range values from the co2 dataset
        if start_year < 1751 or start_year > 2012:
            parser.error("time_range_start must be within the interval 1751 to 2012 for CO2")
        elif end_year < 1751 or end_year > 2012:
            parser.error("time_range_end must be within the interval 1751 to 2012 for CO2")


def create_argparser():
    """
    Creates an argparser from the command line positional parameters

    Arguments:
        data (str): Which of the datasets to be used for the plot, either temperature or co2
        time_range_start (int): What year the plot should start on
        time_range_end (int): What year the plot should end on
        ymin (int): Lowest value for y, the temperature or CO2 value
        ymax (int): Highest value for y, the temperature or CO2 value
        month (str, optional): What month the temperatures should be plotted for, required for temperature

    Returns
        args (argparse Object)
    """
    choices = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December", "All"]
    parser = argparse.ArgumentParser(description="Plots and saves either temperature or CO2 data from CSV files")
    parser.add_argument("data",
                        type=str,
                        choices=["temperature", "co2", "co2_by_country"],
                        help="What data to be used for the plot")
    parser.add_argument("time_range_start",
                        type=int,
                        help="What year the plot should start on. [1812-2012] for temperature, [1751-2012] for CO2")
    parser.add_argument("time_range_end",
                        type=int,
                        help="What year the plot should end on. [1812-2012] for temperature, [1751-2012] for CO2")
    parser.add_argument("ymin",
                        type=int,
                        help="Lowest value for y, the temperature or CO2 value")
    parser.add_argument("ymax",
                        type=int,
                        help="Highest value for y, the temperature or CO2 value")
    parser.add_argument("-month",
                        type=str,
                        default=None,
                        choices=choices,
                        help="What month the temperatures should be plotted for, required for temperature")
    temp_args = parser.parse_args()
    verify_positional_parameters(temp_args, parser)
    return temp_args


def create_smaller_argparser():
    """
        Creates an argparser from the command line positional parameters in the CO2 by Country case

        Arguments:
            data (str): Which of the datasets to be used for the plot, either temperature or co2
            year (int): What year the plot should be for
            thershold (int): What the threshold should be for the CO2 emission

        Returns
            args (argparse Object)
        """
    parser = argparse.ArgumentParser(description="Plots and saves either temperature or CO2 data from CSV files")
    parser.add_argument("data",
                        type=str,
                        choices=["co2_by_country"],
                        help="What data to be used for the plot")
    parser.add_argument("year",
                        type=int,
                        help="What year the plot should be for. [1960-2016]")
    parser.add_argument("threshold",
                        type=float,
                        help="What the threshold should be for the CO2 emission")
    temp_args = parser.parse_args()
    if temp_args.year < 1960 or temp_args.year > 2016:
        parser.error("The year must be within the range 1960 to 2016")
    return temp_args


if __name__ == "__main__":
    if sys.argv[1] != "co2_by_country":
        args = create_argparser()
        if args.data == "temperature":
            plot_temperature((args.time_range_start, args.time_range_end), args.ymin, args.ymax, args.month)
        elif args.data == "co2":
            plot_CO2((args.time_range_start, args.time_range_end), args.ymin, args.ymax)
    else:
        args = create_smaller_argparser()
        plot_CO2_by_country(args.year, args.threshold)
