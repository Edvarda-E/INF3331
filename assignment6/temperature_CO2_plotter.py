import pandas as pd
import argparse
import matplotlib.pyplot as plt


def plot_temperature(year_range, ymin, ymax, month):
    """"
    Module that generates a plot within the provided time- and temperature range, based on the temperature data set
    found in the data directory.

    Arguments:
        year_range (tuple): Start and end year for the plot
        ymin (int): Smallest value for the temperature, meaning the y-axis
        ymax (int): Largest value for the temperature, meaning the y-axis
        month (str): What month to display temperature data for

    Returns:
        Saves the plot with the given boundaries as an image, in the imgs/temp folder
    """
    # Assumption : Display a certain month over the given years in time_range args.month
    # Additional decision: Files overwrite each other by month to keep folder size down
    try:
        # Use pandas to read the csv file, separating values on ,
        temp = pd.read_csv('data/temperature.csv', sep=",")

        # Warns the user if the y-values are completely outside of the data set
        if ymax < temp[month].min():
            print("WARNING: Your ymax value is less than the lowest temperature value in the data set for " + month)
            print("The lowest temperature is " + str(temp[month].min()) + " while you provided the ymax " + str(ymax))
        elif ymin > temp[month].max():
            print("WARNING: Your ymin value is higher than the highest temperature value in the data set for " + month)
            print("The highest temperature is " + str(temp[month].max()) + " while you provided the ymin " + str(ymin))

        plot = temp.plot(
            title="Temperature Plot",
            x='Year',                   # Sets the x-axis to be years
            y=[month],                  # Sets the y-axis to be the temperature for the desired month
            xlim=(year_range[0],        # xlim=(leftmost_value, rightmost_value)
                  year_range[1]),
            ylim=(ymin, ymax),          # ylim=(bottom_value, top_value)
            grid=True
        )
        plot.set_xlabel('Year temperature was measured')
        plot.set_ylabel('Temperature in Degrees Celsius')
        plot.grid(linestyle="dotted")
        # plot is a DataFrame AxesSubplot and has no savefig() module, hence I have to use the pyplot module instead
        plt.savefig('imgs/temp/{}_plot.png'.format(month))
        # plt.show()

    except FileNotFoundError as e:
        print("Couldn't find the temperature data set")


def plot_CO2(year_range, ymin, ymax):
    """
    Module that generates a plot of the CO2 data provided over the time range given.

    Arguments:
        year_range (tuple): Start and end year for plot
        ymin (int): Smallest value for the y-axis
        ymax (int): Largest value for the y-axis

    Returns:
        A plot of the given data
    """
    # Additional decision: Let DataFrame handle the tick rate, despite making the graphs less detailed / decimal values
    # Script warns you if y-values are entirely outside of dataset in your decisions
    # MUST provide ranges :)
    # Year must be different by atleast 1
    try:
        # Use pandas to read the csv file, separating values on ,
        co2_data = pd.read_csv('data/CO2.csv', sep=",")

        # Here I use boolean indexing to extract the parts of the dataframe within the year range only
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
        plt.savefig("imgs/co2/CO2_levels_{}_{}".format(str(year_range[0]), str(year_range[1])))
        plt.show()

    except FileNotFoundError as e:
        print("Couldn't find the temperature data set")


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
    if temp_args.ymin > temp_args.ymax:
        parser.error("The ymin value must be smaller than the ymax value")
    if temp_args.ymin == temp_args.ymax:
        parser.error("Must be atleast one year difference between the year ranges, e.g. 2011 2012")

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
               "November", "December"]
    parser = argparse.ArgumentParser(description="Plots and saves either temperature or CO2 data from CSV files")
    parser.add_argument("data",
                        type=str,
                        choices=["temperature", "co2"],
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


if __name__ == "__main__":
    args = create_argparser()
    if args.data == "temperature":
        plot_temperature((args.time_range_start, args.time_range_end), args.ymin, args.ymax, args.month)
    else:
        plot_CO2((args.time_range_start, args.time_range_end), args.ymin, args.ymax)
