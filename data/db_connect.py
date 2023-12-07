import os
import pymongo as pm
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('data/.env')
load_dotenv(dotenv_path=dotenv_path)


LOCAL = "0"
CLOUD = "1"

USER_DB = 'frontierDB'

client = None

MONGO_ID = '_id'


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    We should probably either return a client OR set a
    client global.
    """
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("CLOUD_MONGO", LOCAL) == CLOUD:
            password = os.environ.get("MONGO_PASSWORD")
            print(password)
            if not password:
                raise ValueError('You must set your password '
                                 + 'to use Mongo in the cloud.')
            print("Connecting to Mongo in the cloud.")
            client = pm.MongoClient(f'mongodb+srv://mmc9967:{password}@frontier.5dsrn7a.mongodb.net/{USER_DB}?retryWrites=true&w=majority')
            # PA recommends these settings:
            # + 'connectTimeoutMS=30000&'
            # + 'socketTimeoutMS=None
            # + '&connect=false'
            # + 'maxPoolsize=1')
            # but they don't seem necessary
        else:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def insert_one(collection, doc, db=USER_DB):
    """
    Insert a single doc into collection.
    """
    return client[db][collection].insert_one(doc)


def fetch_one(collection, filt, db=USER_DB):
    """
    Find with a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        if MONGO_ID in doc:
            # Convert mongo ID to a string so it works as JSON
            doc[MONGO_ID] = str(doc[MONGO_ID])
        return doc


def del_one(collection, filt, db=USER_DB):
    """
    Find with a filter and return on the first doc found.
    """
    return client[db][collection].delete_one(filt)


def fetch_all(collection, db=USER_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=USER_DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc[MONGO_ID]
        ret[doc[key]] = doc
    return ret


def update_doc(collection, filters, update_dict, db=USER_DB):
    return client[db][collection].update_one(filters, {'$set': update_dict})