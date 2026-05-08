from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set

# Create Spark Session with more memory
spark = SparkSession.builder \
    .appName("MarketBasketPreprocess") \
    .master("local[*]") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

print("Spark Session Created!")

# Load only needed columns
order_products = spark.read.csv(
    "data/1_raw/order_products__prior.csv",
    header=True,
    inferSchema=True
).select("order_id", "product_id")

products = spark.read.csv(
    "data/1_raw/products.csv",
    header=True,
    inferSchema=True
).select("product_id", "product_name")

print("Data Loaded!")

# Join data
merged = order_products.join(
    products,
    on="product_id",
    how="inner"
)

print("Join Completed!")

# Reduce partitions
merged = merged.repartition(8)

# Create baskets
baskets = merged.groupBy("order_id") \
    .agg(
        collect_set("product_name").alias("items")
    )

print("Basket Creation Completed!")

# Save directly without show()
baskets.write.mode("overwrite").parquet(
    "data/2_processed/baskets"
)

print("Baskets saved successfully!")