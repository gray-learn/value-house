


def transform_data(data_list, start_year, end_year, min_sale_amount, max_sale_amount):
    
     # Get column structure (list of column names)
    column_structure = data_list.columns.tolist()

    # Remove 'Serial Number' column
    data_list = data_list.drop(columns=['Serial Number'])

    # Filter for rows based on the provided parameters
    data_list = data_list[
        (data_list['List Year'] >= start_year) &
        (data_list['List Year'] <= end_year) &
        (data_list['Sale Amount'] >= min_sale_amount) &
        (data_list['Sale Amount'] <= max_sale_amount) &
        (data_list['Location'].notnull()) &
        (data_list['Non Use Code'].notnull()) &
        (data_list['Address'].notnull()) &
        (data_list['OPM remarks'].notnull()) &
        (data_list['Assessor Remarks'].notnull())
    ]

    # Get the first 5 rows of the filtered dataset
    first_five_rows = data_list.head()

    # Get the total number of rows in the filtered dataset
    total_count = data_list.shape[0]

    # Output results
    print(f"Total dataset count: {total_count}")
    print(" first_five_rows:")
    print(first_five_rows)
    print("Column structure:", column_structure)

    return first_five_rows

