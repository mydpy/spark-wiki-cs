clickstreamRaw = sqlContext.read \
  .format("com.databricks.spark.csv") \
  .options(header="true", delimiter="\t", mode="DROPMALFORMED", inferSchema="true") \
  .load("data/2015_02_clickstream.tsv")
  .cache()
  
# Converts the file to Parquet, an efficient data storage format. 
clickstreamRaw.write \
  .mode("overwrite") \
  .format("parquet") \
  .save("data/2015_02_clickstream.parquet")
  
clicks = sqlContext.read.parquet("data/2015_02_clickstream.parquet").cache()

# Calculate the number of clicks versus the number of Wikipedia clicks
all_clicks = clicks.selectExpr("sum(n) AS clicks").first().clicks
wiki_clicks = clicks.where("prev_id IS NOT NULL").selectExpr("sum(n) AS clicks").first().clicks
float(wiki_clicks) / all_clicks * 100

# Make clicks available as a SQL table.
clicks.registerTempTable("clicks")