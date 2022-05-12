import json
import pymongo
from bson import ObjectId
from copy import deepcopy


MONGO_CONNECTION = 'mongodb://192.168.44.112:27017/'
TELEMETRY_HUB_DB = 'TelemetryHub'
PAYLOAD = {
    'farm_job_id': '',
    'json_data': ''
}


def get_payload(farm_job_id):
    payload = deepcopy(PAYLOAD)
    found_json_data = _get_farm_job_id_json(farm_job_id)
    if found_json_data:
        payload['farm_job_id'] = farm_job_id
        payload['json_data'] = json.dumps(found_json_data, indent=4)
    return payload


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def _get_farm_job_id_json(farm_job_id):
    db = _get_mongo_db_obj()
    collection = db['farm_jobs']
    cursor = collection.find({})
    for document in cursor:
        if 'farm_job_id' in document.keys() and document['farm_job_id'] == farm_job_id:
            json_str = JSONEncoder().encode(document)
            return json.loads(json_str)
    return None


def _get_mongo_db_obj():
    client = pymongo.MongoClient(MONGO_CONNECTION)
    return client[TELEMETRY_HUB_DB]


def get_empty_payload():
    return deepcopy(PAYLOAD)
