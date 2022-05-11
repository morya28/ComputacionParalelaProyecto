from copy import deepcopy


PAYLOAD = {
    'farm_job_id': '',
    'service': '',
    'env_type': '',
    'family': '',
    'test_case': '',
    'json_type': '',
    'date': '',
    'json_data': ''
}


def get_payload(farm_job_id):
    """ """
    payload = deepcopy(PAYLOAD)
    if farm_job_id == 'foobar':
        payload['json_data'] = 'DIOOOOOOO!'
    return payload


def get_empty_payload():
    """ """
    return deepcopy(PAYLOAD)
