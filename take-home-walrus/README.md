# Take-Home Walrus Project

This project extracts data from QUALYS, and CROWDSTRIKES API, normolizes the data,
implements a MongoDB storage system and a data deduplication pipeline with error handling and exception logging. 
It includes unit tests for the storage functionality and extractors functionality using `pytest` and `unittest.mock`.

## Prerequisites

- Python 3.10 or later
- MongoDB server (local or remote)
- Python packages from `requirements.txt`

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/take-home-walrus.git
   cd take-home-walrus

2. Install Dependencies
pip install -r requirements.txt

3. Set up configuration: Modify the config.py file with your MongoDB details:
# config.py
MONGO_DB_URL = "mongodb_url"
DB_NAME = "database_name"
DB_COLLECTION = "collection_name"

4. Running the Project

py mongodb_storage.py to persist deduplicated host
py main.py to run overall project

5. Running Unit tests

pytest


### TO MAKE THIS SCALABLE FOR HANDELING TERRABYTES OF DATA ###

Scalable Data Ingestion:

We could use distributed message queues like Apache Kafka or AWS Kinesis to handle high-throughput data ingestion.
Implement asynchronous processing with tools like asyncio to manage multiple data streams concurrently.

Distributed and Scalable Storage:

We can store large datasets in data lakes (e.g., Amazon S3, Google Cloud Storage or HDFS) for cheap, scalable storage.
Utilizing NoSQL databases (e.g., MongoDB, Cassandra) for real-time access and horizontal scalability.
For batch processing, we can use Hadoop, its HDFS can distribute large files across nodes.

Parallel and Distributed Data Processing:

I would use Apache Spark for distributed and parallel processing, which is optimized for large datasets.
With this we can implement data partitioning for parallel reads/writes and distribute processing across nodes.

Indexing and Query Optimization:

We could use indexing and partitioned queries to optimize data retrieval and speed up search performance, especially on large datasets.

Horizontal Scaling:

Horizontal Scaling would be good choice to enhance the performance. We can use container orchestration tools like Kubernetes for scaling applications across multiple nodes.
And we can employ load balancers to distribute tasks evenly across servers and ensure fault tolerance.




