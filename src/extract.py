import pandas as pd

def extract_data(csv_url):
    # Adjust the display option to show all columns
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.expand_frame_repr', False)  # Avoid line wrapping

    # Read your CSV data
    data_list = pd.read_csv(csv_url, low_memory=False)
    return data_list