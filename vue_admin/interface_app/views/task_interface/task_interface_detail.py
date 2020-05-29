


from interface_app.froms.task_form import TaskInterfaceFrom
from interface_app.models.task import TaskInterface
from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_detail import MyBaseDetailView


class TaskInterfaceDetailView(MyBaseDetailView):
    model = TaskInterface
    form = TaskInterfaceFrom
    eCode = ErrorCode.task_interface


