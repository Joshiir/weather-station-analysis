import json


def str_to_int(x):
    """
    This function accepts a string and returns
    an integer, returns -1 if there is an error.
    """
    try:
        integer = int(x)
        return integer
    except ValueError:
        return -1

# Test Inputs
#
# print(str_to_int("12345"))
# print(type(str_to_int("12345")))


def str_to_float(x):
    """
    This function accepts a string and returns
    a float, returns -1.0 if there is an error.
    """
    try:
        flt = float(x)
        return flt
    except ValueError:
        return -1.0

# Test inputs
#
# print(str_to_float("12345"))
# print(type(str_to_float("12345")))


def month_to_int(month, input_str):
    """
    Accepts month prefix and returns it as
    its respective integer, returns -1 if there
    is an error.
    """
    for c in input_str:
        c = input_str
        if c not in month.keys():
            return -1
        else:
            i = month[c]
            output_int = int(i)
        return output_int


month = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

# Test inputs
#
# print(month_to_int(month, "Jun"))
# print(type(month_to_int(month, "Jun")))


class Measurement:
    """
    A class that contains the year,
    month, and value of rainfall.
    """
    def __init__(self, year, month, value):
        self.year = year
        self.month = month
        self.value = value

    def __repr__(self):
        """
        Returns data members in year, month
        and value within a string.
        """
        return f"Year:{self.year}, Month:{self.month}, Value:{self.value}mm"

    def from_strings(self, year_str, month_str, value_str):
        """
        The function converts the Year and Month input
        from strings to integers and Value from
        string to float. Returns true if
        conversion was successful and false
        if it fails.
        """
        for x in year_str:
            year_int = str_to_int(x)
            inst_year = isinstance(year_int, int)
            if inst_year is True:
                return self.year
            else:
                return print("Year conversion failed")

        for y in month_str:
            month_int = month_to_int(month, y)
            inst_month = isinstance(month_int, int)
            if inst_month is True:
                return self.month
            else:
                return print("Month conversion failed")

        for z in value_str:
            val_float = str_to_float(z)
            inst_val = isinstance(val_float, float)
            if inst_val is True:
                return self.value
            else:
                return print("Value conversion failed")


class WeatherStation:
    """
    A class stores the station id
    and list of measurements.
    """
    def __init__(self, id=0):
        self.id = id
        self.measurements = []

    def __repr__(self):
        """
        Returns data members in id
        and measurements within a string.
        """
        return f"Station ID:{self.id}, Measurements:{self.measurements}."

    def from_json(self, json_data):
        """
        This function accepts JSON data as an input,
        checks for one key value, and splits the month
        and year into individual values.
        """
        data = json_data
        key = data.keys()
        num = 0
        self.id = list(data.keys())[0]

        if len(key) == 1:
            print("The number of keys is", + len(key))
            return True
        elif len(data.keys()) != 1:
            print("The number of keys exceeds 1")
            return False

        for timestamp in data.values():
            for element in timestamp:
                for i in element.values():
                    if num == 0:
                        month = (i[0:4])
                        year = str(i[4:])
                        num += 1
                    else:
                        if num == 1:
                            value = i
                            num = 0
                        measure = Measurement(year, month, value)
                        self.measurements.append(measure)
                        return self.measurements

    def years(self, json_data):
        """
        Accepts JSON file, and sorts only the years
        so they appear once in a list.
        """
        data = json_data
        years_list = []

        for value in data.values():
            for val in value:
                years_list.append(val["Timestamp"][4:])
        unsorted_years = set(years_list)
        years_list = sorted(unsorted_years)
        return years_list

    def maximum_per_year(self, json_data):
        """
        Accepts JSON file, and loops through
        the year and values to sort by the
        maximum value per year.
        """
        data = json_data
        max_values = {}
        num = 0
        val = data[str(self.id)][0]
        year = int(val["Timestamp"][4:])
        while num < len(data[str(self.id)]):
            index = data[str(self.id)][num]
            yr = int(index["Timestamp"][4:])
            lst = []
            max_val = 0
            while int(year) == int(yr) and num < len(data[str(self.id)]):
                index = data[str(self.id)][num]
                year = index["Timestamp"][4:]
                measurement = index["Value"]
                lst.append(float(measurement))
                num += 1
            max_val = max(lst)
            max_values[yr] = int(float(max_val))
        return max_values


def read_json(file_name):
    """
    A function to read a JSON file into memory.
    """
    input_file = open(file_name, "r", encoding="utf-8")
    json_data = json.load(input_file)
    input_file.close()
    return json_data


"""
A Program that loads the JSON file and
prints a string, years and maximum years.
"""
if __name__ == "__main__":

    json_data = read_json("rainfall.json")

    station = WeatherStation()
    print(station.from_json(json_data))
    print(station.years(json_data))
    print(station.maximum_per_year(json_data))
