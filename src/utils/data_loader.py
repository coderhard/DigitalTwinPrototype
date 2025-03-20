from fileinput import filename
import pandas as pd
import logging
import os  # Import the os module

def load_dataset(filename: str) -> pd.DataFrame:
    """
    Loads a CSV dataset into a pandas DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame, or None if an error occurs.
    """
    
    # Construct the relative path to the datasets directory
    #base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    datasets_dir = os.path.join(base_dir, 'datasets')
    filepath = os.path.join(datasets_dir, filename)

    try:
        logging.info(f"Attempting to load dataset from: {filepath}")
        logging.info(f"Current working directory: {os.getcwd()}")  # Log the current working directory
        logging.info(f"Checking if file exists: {os.path.exists(filepath)}")  # Check if the file exists
        df = pd.read_csv(filepath)
        logging.info(f"Dataset loaded successfully from: {filepath}")
        return df
    except FileNotFoundError:
        logging.error(f"Error: Dataset file not found at: {filepath}")
        return None
    except pd.errors.EmptyDataError:
        logging.error(f"Error: Dataset file is empty: {filepath}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while loading the dataset: {e}")
        return None

if __name__ == "__main__":
    # Configure logging (We will change to app level logging in the future)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    shipyard_data = load_dataset("Digital_Shipyard_50k_With_Attacks.csv")
    if shipyard_data is not None:
        print("Shipyard data loaded successfully.")
        # TODO: perform further operations on the DataFrame here
    else:
        print("Shipyard data loading failed.")

    supply_chain_data = load_dataset("Supply_Chain_50k_With_Attacks.csv")
    if supply_chain_data is not None:
        print("Supply chain data loaded successfully.")
    else:
        print("Supply chain data loading failed.")