df = spark \
.read \
.format("csv") \
.option("header", True) \
.option("inferSchema", True) \
.option("delimiter",";") \
.load("s3://datalake-pedrosa-524095156763/raw/enem/enem_csv/dataload=20230131/microdados_enem_2020.csv")

df \
.write \
.mode("overwrite") \
.format("parquet") \
.save("s3://datalake-pedrosa-524095156763/consumer_zone/enem/dataload=20230131")
