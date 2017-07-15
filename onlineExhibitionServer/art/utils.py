__author__ = 'huangzhongkai'
import requests
import json
import time
import hashlib


class Wx(object):

    def __init__(self, appid, appsecret, url):
        self.appid = appid
        self.appsecret = appsecret
        self.url = url
        self.timestamp = str(time.time()).split('.')[0]
        self.noncestr = 'Wm3WZYTPz0wzccnW'
        print self.appid, self.appsecret,self.url

    def get_access_token(self):
        r = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + self.appid +
                             '&secret=' + self.appsecret)
        access_token = r.json()['access_token']
        return access_token

    def get_jsapi_ticket(self):
        r = requests.get(url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=' + self.get_access_token() +
                             '&type=jsapi')
        if r.json()['errcode'] == 0:
            jsapi_ticket = r.json()['ticket']
            print jsapi_ticket
            return jsapi_ticket
        else:
            return -1

    def get_signature(self):
        noncestr = self.noncestr
        url = self.url
        timestamp = self.timestamp

        if self.get_jsapi_ticket() != -1:
            joint_string = 'jsapi_ticket=' + self.get_jsapi_ticket() + '&noncestr=' + noncestr + '&timestamp=' + \
                           timestamp + '&url=' + url
            print joint_string

            signature = hashlib.sha1(joint_string).hexdigest()
            print signature
            return signature