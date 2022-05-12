import json
from copy import deepcopy


PAYLOAD = {
    'farm_job_id': '',
    'json_data': ''
}


def get_payload(farm_job_id):
    payload = deepcopy(PAYLOAD)
    if farm_job_id == 'foobar':
        payload['farm_job_id'] = farm_job_id
        json_data = '{"name": "DIOOOOOOO!", "ora": "ora", "ora1": "ora", "ora2": "ora", "ora3": "ora", "ora4": {"foo": "bar"}}'
        json_data = json.loads(json_data)
        payload['json_data'] = json.dumps(json_data, indent=4)
    return payload


def get_empty_payload():
    return deepcopy(PAYLOAD)
