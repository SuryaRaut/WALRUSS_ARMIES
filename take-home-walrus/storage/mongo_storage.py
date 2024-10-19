from pymongo import MongoClient
from config import MONGO_DB_URL, DB_NAME, DB_COLLECTION

def fetch_mongo_db_client():
    try:
        client = MongoClient(MONGO_DB_URL)
        print(client.list_database_names())
        print("Connection Successfull!")
        return client
    except Exception as e:
        print("Error Connection MongoDb:", e)

def persist_dedups_hosts(hosts: list):
    if not hosts:
        print(f"No Hosts to persist, empty list.")
        return
    clients = fetch_mongo_db_client()
    db = clients[DB_NAME]
    collections = db[DB_COLLECTION]
    try:
        reslt = collections.insert_many(hosts)
        print(f"Peristed {len(reslt.inserted_ids)} docs into mongodb")
    except Exception as ex:
        print(f"Error persisting into mongodb: {ex}")
    finally:
        clients.close()