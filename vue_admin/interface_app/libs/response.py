from django.http import JsonResponse
from logout import info
class ErrorCode:
    common = 10000
    auth = 10001
    service = 10002
    task = 10003
    interface = 10003
    task_interface = 10004

def common_response(success,data,error_code,error_msg,log_tag=""):
    response = {
        "data":data,
        "success":success,
        "error":{
            "code":error_code,
            "msg":error_msg
        }
    }
    info("<=={}，返回body:{}".format(log_tag,str(response)))
    return JsonResponse(response,safe=False)


def response_success(data={},log_tag=""):
    return common_response(True,data,"","",log_tag=log_tag)


def response_failed(code=ErrorCode.common,message="参数错误",data={},log_tag=""):

    return common_response(False,data,code,message,log_tag)