import json
from django.forms import model_to_dict
from interface_app.froms.task_form import TaskForm, TaskInterfaceFrom
from interface_app.libs.response import ErrorCode, response_success, response_failed
from interface_app.models.task import TaskInterface
from interface_app.models.interface import Interface
from interface_app.views.base.base_list import MyBaseListView
from logout import info

class TaskInterfaceListView(MyBaseListView):

    model = TaskInterface
    form = TaskInterfaceFrom
    eCode = ErrorCode.task_interface

    def get(self, request, *args, **kwargs):
        """
        这个是获取列表数据，需要一个参数：task_id在url里面
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        task_id = request.GET.get("task_id", 0)
        info("拿到GET数据，判断获取的数据类型为{}".format(request.GET))
        if not isinstance(task_id,int):
            return response_failed()

        task_interfaces = TaskInterface.objects.filter(task_id=task_id)
        info("根据任务ID{},获取接口：{}".format(task_id,task_interfaces))
        ret = []
        for s in task_interfaces:

            interface = Interface.objects.filter(id=s.interface_id).first()
            interface_dict = model_to_dict(interface)
            interface_dict["context"]=json.loads(interface_dict["context"],encoding="utf-8")
            ret.append(interface_dict)

        return response_success(data=ret)


    def post(self, request, *args, **kwargs):
        """
        这个是创建列表数据，新增任务id和接口id的关联关系记录[{}]
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        info("123")
        body = request.body
        info("拿到body数据，判断body数据类型为{}".format(type(body)))
        data = json.loads(body, encoding='utf-8')
        if "context" not in data:
            return response_failed()

        info("获取传入的context值{},类型为{}".format(data["context"],type(data["context"])))
        data["context"] = json.dumps(data["context"],encoding="utf-8")
        form = self.form(data)

        info("入参{}".format(form))
        if not form.is_valid():
            return response_failed()

        # user = Service.objects.create(name=form.cleaned_data["name"],description=form.cleaned_data["description"])
        _data = self.model.objects.create(**form.cleaned_data)

        if not _data:
            return response_failed(code=self.eCode, message='创建失败，请联系开发小朋友')
        else:
            return response_success()
