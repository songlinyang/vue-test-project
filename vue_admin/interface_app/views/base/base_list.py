import json

from django.forms import model_to_dict
from django.views.generic import View
from interface_app.froms.service_form import ServiceForm
from interface_app.froms.service_form import ServiceForm
from interface_app.libs.response import response_success, response_failed
from interface_app.models.service import Service
from interface_app.libs.response import ErrorCode
from logout import info

class MyBaseListView(View):
    model = Service
    form = ServiceForm
    eCode = ErrorCode.service

    def get(self, request, *args, **kwargs):
        """
        这个是获取列表数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        info("进入了获取数据接口")
        # 获取数据
        base_data = self.model.objects.all()

        # 组装数据
        ret = []
        for data in base_data:
            ret.append(model_to_dict(data))
        # 返回数据
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        这个是创建列表数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        info("进入了创建数据接口")
        body = request.body
        data = json.loads(body, encoding='utf-8')
        form = self.form(data)
        
        if not form.is_valid():
            return response_failed()

        # user = Service.objects.create(name=form.cleaned_data["name"],description=form.cleaned_data["description"])
        base_data = self.model.objects.create(**form.cleaned_data)

        if not base_data:
            return response_failed(code=self.eCode, message='创建失败，请联系开发小朋友')
        else:
            return response_success()