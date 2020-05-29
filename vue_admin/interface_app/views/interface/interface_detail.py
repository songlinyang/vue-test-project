import json

from django.forms import model_to_dict

from interface_app.froms.interface_form import InterfaceForm
from interface_app.libs.response import response_success, response_failed
from interface_app.models.interface import Interface
from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_detail import MyBaseDetailView


class InterfaceDetailView(MyBaseDetailView):

    model = Interface
    form = InterfaceForm
    eCode = ErrorCode.interface



    def get(self, request, base_id, *args, **kwargs):
        """
        这个是获取单个列表的数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        s = self.model.objects.filter(id=base_id).first()

        if not s:
            return response_failed("数据不存在")
        s_dict = model_to_dict(s)
        s["context"] = json.loads(s["context"], encoding='utf-8')
        return response_success(s_dict)

    def put(self, request, base_id, *args, **kwargs):
        """
        这个是全量修改数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding='utf-8')


        data["context"] = json.dumps(data["context"])
        form = self.form(data)
        if not form.is_valid():
            return response_failed()
        # 1.先查询一遍数据是否存在
        # user = self.model.objects.create(name=form.cleaned_data["name"],description=form.cleaned_data["description"])
        base_data = self.model.objects.filter(id=base_id).first()
        if not base_data:
            return response_failed(code=self.eCode, message='数据不存在')
        # 若存在,update
        self.model.objects.filter(id=base_id).update(**form.cleaned_data)

        # 再次查询
        s = self.model.objects.filter(id=base_id).first()
        s_dict = model_to_dict(s)
        return response_success(s_dict)


    def delete(self, reqeust, base_id, *args, **kwargs):
        """
        这个是删除数据
        :param reqeust:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        base_data = self.model.objects.filter(id=base_id).first()
        if not base_data:
            return response_failed(code=self.eCode,message="数据不存在，无法删除")
        base_data.delete()
        base_data.save()
        return response_success()


