from django.http import HttpResponse
from django.shortcuts import render

from telemetryhub.mongodb_config import mongodb_utils


def telemetry_hub(request, farm_job_id="", service="", env_type="", family="",
                  test_case="", json_type="", json_data=None):
    parameters = {
        'farm_job_id': farm_job_id,
        'json_data': json_data
    }
    return render(request, 'telemetry_hub.html', parameters)


def search_id(request):
    if request.GET['farm_job_id']:
        farm_job_id = request.GET['farm_job_id']
        return render(
            request, 'telemetry_hub.html',
            mongodb_utils.get_payload(farm_job_id)
        )
    return render(
        request, 'telemetry_hub.html',
        mongodb_utils.get_empty_payload()
    )
