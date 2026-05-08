import os
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# Load environment variables
load_dotenv()

def fetch_kaggle_data(dataset_name, output_dir):

    print(f"Downloading dataset: {dataset_name}")

    os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
    os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

    api = KaggleApi()
    api.authenticate()

    os.makedirs(output_dir, exist_ok=True)

    api.dataset_download_files(
        dataset_name,
        path=output_dir,
        unzip=True
    )

    print("Download completed!")

if __name__ == "__main__":

    DATASET = "psparks/instacart-market-basket-analysis"

    RAW_DIR = "data/1_raw"

    fetch_kaggle_data(DATASET, RAW_DIR)