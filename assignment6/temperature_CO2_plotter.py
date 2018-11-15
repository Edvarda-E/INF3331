import pandas as pd
import argparse
import matplotlib.pyplot as plt

def plot_temperature(time_range, ymin, ymax, month):
    """"
    Module that generates a plot of the temperature data provided over the month given.

    Arguments:
        time_range (tuple): Start and end year for plot
        ymin (int): Smallest value for the y-axis
        ymax (int): Largest value for the y-axis
        month (str): What month to display temperature data for

    Returns:
        Saves a plot of the given data
    """
    # Assumption : Display a certain month over the given years in time_range args.month
    temp = pd.read_csv('data/temperature.csv', sep=",")
    plot = temp.plot(
        x='Year',               # Sets the x-axis to be years
        y=['January'],          # Sets the y-axis to be the desired month
        xlim=(time_range[0],    # xlim=(leftmost_value, rightmost_value)
              time_range[1]),
        ylim=(ymin, ymax)       # ylim=(bottom_value, top_value)
    )
    plot.set_xlabel('Year Temperature was Measured')
    plot.set_ylabel('Temperature in Degrees Celsius')
    plt.show()


def plot_CO2(time_range, ymin, ymax, plot_data):
    """
    Module that generates a plot of the CO2 data provided over the time range given.

    Arguments:
        time_range (tuple): Start and end year for plot
        ymin (int): Smallest value for the y-axis
        ymax (int): Largest value for the y-axis
        plot_data (dict): CO2 data to be plotted

    Returns:
        A plot of the given data
    """
    pass


def verifiy_positional_parameters(temp_args, parser):
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
    else: # co2 is the data
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
    verifiy_positional_parameters(temp_args, parser)
    return temp_args


if __name__ == "__main__":
    args = create_argparser()
    if args.data == "temperature":
        plot_temperature((args.time_range_start, args.time_range_end), args.ymin, args.ymax, args.month)
    else:
        pass
