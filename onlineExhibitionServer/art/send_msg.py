# -*- coding: utf-8 -*-
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
import json
import random

reload(sys)
sys.setdefaultencoding('utf8')

REGION = "cn-hangzhou"
ACCESS_KEY_ID = "LTAIqs5tTEPT3q1R"
ACCESS_KEY_SECRET = "6wHKVutnmQBwa7minBGJ1VzslSTmkN"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    smsRequest.set_TemplateCode(template_code)

    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    smsRequest.set_OutId(business_id)

    smsRequest.set_SignName(sign_name);

    smsRequest.set_PhoneNumbers(phone_numbers)

    smsResponse = acs_client.do_action_with_exception(smsRequest)


    return smsResponse


def query_send_detail(biz_id, phone_number, page_size, current_page, send_date):
    queryRequest = QuerySendDetailsRequest.QuerySendDetailsRequest()
    queryRequest.set_PhoneNumber(phone_number)
    queryRequest.set_BizId(biz_id)
    queryRequest.set_SendDate(send_date)
    queryRequest.set_CurrentPage(current_page)
    queryRequest.set_PageSize(page_size)

    queryResponse = acs_client.do_action_with_exception(queryRequest)


    return queryResponse


# __name__ = 'send'
# if __name__ == 'send':
#     __business_id = uuid.uuid1()
#     print __business_id
#     code = str(random.randrange(100000, 999999, 6))
#     params = {"code":code}
#     print send_sms(__business_id, "15725453540", "艺术展厅app", "SMS_91030041", json.dumps(params))

# if __name__ == 'query':
#     print query_send_detail("1234567^8901234", "13000000000", 10, 1, "20170612")
