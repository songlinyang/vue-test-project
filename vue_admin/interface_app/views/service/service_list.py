

from interface_app.froms.service_form import ServiceForm
from interface_app.models.service import Service
from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_list import MyBaseListView


class ServiceListView(MyBaseListView):

    model = Service
    form = ServiceForm
    eCode = ErrorCode.service



