def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   column=data.split('\n')
   com_fir=column[0].split(',')
   return com_fir
f=open('data.csv')
print(get_first_row(f.read()))
# Read the csv file