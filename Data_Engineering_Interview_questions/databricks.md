1. What is delta load (or incremental load)?
Answer: Also known as incremental load. An effiecient ETL process that extracts, transform and loads only new, modified or deleted data since the last update rather than processing the entire dataset with timestamps, incremental IDs or CDC(Change Data Capture) mechanisms often involves the merge statements in the sink (source) systems.

2. What is full load?
Answer: Full load is the type of the data ingestion in which entire data is transafered from source to sink replacing the existing data generally used in the initial small loads, slowly-changing datasets ensures the data consistency is resource-intensive and slow compared to the incremental load or delta load.

3. What is the Azure Data Factory?
Answer: Used for the ETL/ELT data integration, ingestion, orchestration in the data warehouse.

4. What did you used the data warehousing?
Answer: Azure synapse analytics is the coure engine that integration, warehousing and big data processing and also containing the machine learning, business intelligence (BI Tools), azure data lake storage and azure data factory.

5. What are the key components and services of the Azure synapse?
i. Azure Synapse Analytics: The core engine that combines data integration, warehousing and big data processing.
ii. Azure data factory: Used for the ETL/ELT data integration, ingestion, orchestration in the data warehouse.
iii. Azure data lake storage: Serves as landing zone for raw data before loading into synapse.
vi. Power BI: Integrates with synapse for data visualization and reporting.

6. While you trigger pipelines within ADF to run the databricks jobs does there need to install libraries?
Answer: Yes, In the ADF activity to execute the Databricks Notebook/Jar/Python you have opportunity that you would like to install the libraries on cluster suitable for the single activity but cumbersome if you have many activities or many libraries.

7. If there is problem for many activities or many libraries then how do you solve?
Answer: In databricks, you can navigate to the task section of the job and first task of your job, under the task properties you would see dependant libraries using which you can install dependant libraries for maven, python or custom jar.