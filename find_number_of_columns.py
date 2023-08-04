import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    rows=data.split('\n')
    bir_row=rows[0].split(',')
    return len(bir_row)
f=open('data.csv')
print(find_number_of_columns(f.read()))
# Read the csv file