import yaml
from extract import extract_data
import sys
from transform import transform_data
# from load import load_to_s3

def load_config():
    with open('config/config.yaml','r') as file:
        return yaml.safe_load(file)

def etl():
    config = load_config()
    # Get parameters from command line arguments
    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])
    min_sale_amount = float(sys.argv[3])
    max_sale_amount = float(sys.argv[4])

    price_list = extract_data(config['url'])

    transform_data(price_list, start_year, end_year, min_sale_amount, max_sale_amount)

    # load_to_s3(transform_data, config['s3_bucket'], config['s3_file_name'])

if __name__ == "__main__":
    etl()
