from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import concat_ws

# Create Spark Session
spark = SparkSession.builder \
    .appName("MarketBasketFPgrowth") \
    .master("local[*]") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

print("Spark Session Created!")

# Load baskets
baskets = spark.read.parquet(
    "data/2_processed/baskets"
)

print("Basket data loaded!")

# FP-Growth model
fpGrowth = FPGrowth(
    itemsCol="items",
    minSupport=0.01,
    minConfidence=0.3
)

print("Training FP-Growth model...")

model = fpGrowth.fit(baskets)

print("Model training completed!")

# Frequent Itemsets
freq_itemsets = model.freqItemsets.withColumn(
    "items",
    concat_ws(", ", "items")
)

# Association Rules
association_rules = model.associationRules \
    .withColumn(
        "antecedent",
        concat_ws(", ", "antecedent")
    ) \
    .withColumn(
        "consequent",
        concat_ws(", ", "consequent")
    )

# Save outputs
freq_itemsets.write.mode("overwrite").csv(
    "data/3_output/frequent_itemsets",
    header=True
)

association_rules.write.mode("overwrite").csv(
    "data/3_output/association_rules",
    header=True
)

print("Association rules saved successfully!")

# Show sample
association_rules.show(10, truncate=False)