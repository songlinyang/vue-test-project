import json

from django.forms import model_to_dict

from interface_app.froms.interface_form import InterfaceForm
from interface_app.models.interface import Interface
from interface_app.libs.response import ErrorCode, response_success, response_failed
from interface_app.views.base.base_list import MyBaseListView
from logout import info


class InterfaceListView(MyBaseListView):

    model = Interface
    form = InterfaceForm
    eCode = ErrorCode.interface

    def get(self, request, *args, **kwargs):
        """
        这个是获取单个服务下的接口数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 获取数据
        service_id = request.GET.get("service_id",0)
        info("获取到的服务ID{}".format(service_id))
        if not service_id:
            return response_failed()

        interface = self.model.objects.filter(service_id=int(service_id))

        # 组装数据
        ret = []
        for i in interface:
            t = model_to_dict(i)
            t['context'] = json.loads(t['context'],encoding='utf-8')
            ret.append(t)

            #ret.append(model_to_dict(s))
        # 返回数据
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        这个是创建单个服务下的接口数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        body = request.body

        data = json.loads(body, encoding='utf-8')
        if "context" not in data:
            return response_failed(log_tag="新增接口,判断context是否存在")

        info("获取传入的context值{},类型为{}".format(data["context"], type(data["context"])))
        data["context"] = json.dumps(data["context"])
        info("data{},类型为{}".format(data, type(data)))
        form = self.form(data)


        if not form.is_valid():

            return response_failed(log_tag="新增接口,判断is_valid")

        _data = self.model.objects.filter(name=data["name"],service_id=data["service_id"]).first()
        if _data:
            return response_failed(log_tag="新增接口",message="无法新增重复数据")
        # user = Service.objects.create(name=form.cleaned_data["name"],description=form.cleaned_data["description"])
        _data = self.model.objects.create(**form.cleaned_data)
        info("入数据库成功")
        if not _data:
            response = response_failed(code=self.eCode, message='创建失败，请联系开发小朋友')
            return response
        else:
            return response_success()

