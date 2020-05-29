import json

from django.forms import model_to_dict
from django.views.generic import View
from interface_app.froms.service_form import ServiceForm
from interface_app.froms.service_form import ServiceForm
from interface_app.libs.response import response_success, response_failed
from interface_app.models.service import Service
from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_detail import MyBaseDetailView


class ServiceDetailView(MyBaseDetailView):

    model = Service
    form = ServiceForm
    eCode = ErrorCode.service


