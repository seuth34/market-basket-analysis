import os

def test_raw_data_exists():

    assert os.path.exists("data/1_raw/products.csv")

def test_processed_data_exists():

    assert os.path.exists("data/2_processed/baskets")

def test_output_exists():

    assert os.path.exists("data/3_output/association_rules")