import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import org.apache.spark.graphx.lib.PageRank
import org.apache.spark.graphx.lib.ShortestPaths
import org.apache.spark.sql._
import org.apache.spark.sql.types.{StructType,StructField,StringType}

  val clickstreamDF = sqlContext.read.format("com.databricks.spark.csv")
    .option("header", "true")
    .option("delimiter", "\\t")
    .option("mode", "PERMISSIVE")
    .option("inferSchema", "true")
    .load("/Users/mbaker003c/spark/data/2015_02_clickstream.tsv")
    .where("n > 100")
    .cache()