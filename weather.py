import csv
from datetime import datetime
from textwrap import dedent, indent

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp): #DONE
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string containing the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# print(format_temperature("80"))

def convert_date(iso_string): #DONE
    dt = datetime.fromisoformat(iso_string)
    day = dt.strftime("%A")
    date = dt.strftime("%d")
    month = dt.strftime("%B")
    year = dt.strftime("%Y")

    return(f"{day} {date} {month} {year}")
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

# print(convert_date("2021-07-02T07:00:00+08:00"))

def convert_f_to_c(temp_in_farenheit): #DONE
    c_temp = (float(temp_in_farenheit) - 32) * 5 / 9
    c_temp = round(c_temp, 1)
    return c_temp
    """Converts a temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

def calculate_mean(weather_data): #DONE
    sum = 0
    counter = 0
    mean = 0
    for value in weather_data:
        sum += float(value)
        counter += 1
        mean = sum / counter
    return mean

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

# print(calculate_mean([49, 57, 56, 55, 53]))

def load_data_from_csv(csv_file): #DONE
    list = []
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)
        for line in reader:
            if len(line) != 0:
                list.append([line[0], int(line[1]),int(line[2])])
    return list
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

# print(load_data_from_csv("/Users/amandacook/Desktop/She Codes/GIT/she-codes-python/Project/she-codes-python-weather-project-mandydc10/tests/data/example_two.csv"))

def find_min(weather_data): #DONE
    min_num = 150
    min_index = None

    if len(weather_data) == 0: 
        return ()  
    else:
        for num in range(len(weather_data)):
            value = float(weather_data[num])
            if value <= min_num:
                min_num = value
                min_index = num

    return min_num, min_index

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass

def find_max(weather_data): #DONE
    max_num = -150
    max_index = None

    if len(weather_data) == 0:
        return ()  
    else:
        for num in range(len(weather_data)):
            value = float(weather_data[num])
            if value >= max_num:
                max_num = value
                max_index = num
    return max_num, max_index
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data): #DONE
    lowest_temps_list = []
    highest_temps_list = []
    num_of_days = len(weather_data)
    
    # Loop through weather data to create new lists for hottest / coldest temps
    for line in weather_data:
        lowest_temps_list.append(line[1])
        highest_temps_list.append(line[2])
    
    # Capture info for hottest day 
    hottest_day_data = find_max(highest_temps_list)
    hottest_temp = hottest_day_data[0]
    hottest_temp_in_c = format_temperature(convert_f_to_c(hottest_temp))
    hottest_day = weather_data[hottest_day_data[1]][0]
    hottest_day_string = convert_date(f"{hottest_day}")

    # Capture info for coldest day 
    coldest_day_data = find_min(lowest_temps_list)
    coldest_temp = coldest_day_data[0]
    coldest_temp_in_c = format_temperature(convert_f_to_c(coldest_temp))
    coldest_day = weather_data[coldest_day_data[1]][0]
    coldest_day_string = convert_date(f"{coldest_day}")

    # Capture the averages
    average_low = format_temperature(convert_f_to_c(calculate_mean(lowest_temps_list)))
    average_high = format_temperature(convert_f_to_c(calculate_mean(highest_temps_list)))

    # Formatted Output
    summary = f"{num_of_days} Day Overview\n  The lowest temperature will be {coldest_temp_in_c}, and will occur on {coldest_day_string}.\n  The highest temperature will be {hottest_temp_in_c}, and will occur on {hottest_day_string}.\n  The average low this week is {average_low}.\n  The average high this week is {average_high}.\n"
    
    return summary

# generate_summary(load_data_from_csv("tests/data/example_three.csv"))

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

def generate_daily_summary(weather_data): #unfinished, center alignment needed
    daily_summary_list = ""
    date = None
    min_temp = 0
    max_temp = 0

    for item in range(len(weather_data)):
        min_temp = format_temperature( convert_f_to_c(weather_data[item][1]))
        max_temp = format_temperature( convert_f_to_c(weather_data[item][2]))
        date = convert_date(weather_data[item][0])
        summary = f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        # print(f"{summary}\n")
        daily_summary_list += f"{summary}"
    
    print(daily_summary_list)
    return daily_summary_list
        
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

generate_daily_summary(load_data_from_csv("tests/data/example_one.csv"))
