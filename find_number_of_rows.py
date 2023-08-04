import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    rows=data.split('\n')
    for i in rows:
        print(i)
    return len(rows)
f=open('data.csv')
print(find_number_of_rows(f.read()))
# Read the csv file
