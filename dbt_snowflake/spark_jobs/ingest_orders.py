from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("local_ingestion").getOrCreate()

orders = spark.read.csv("data/orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)

orders_clean = orders.filter(F.col("order_id").isNotNull()) \
        .withColumn("amount_usd",F.col("amount_cents") / 100)
orders_clean.write.mode("overwrite").parquet("data/bronze/orders/")
customers.write.mode("overwrite").parquet("data/bronze/customers/")
print("Ingestion completed successfully.")