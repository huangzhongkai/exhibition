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
        self.noncestr = 'WecWkTYHZw4WRR0f'
        print self.appid, self.appsecret,self.url

    def get_access_token(self):
        r = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + self.appid +
                             '&secret=' + self.appsecret)
        access_token = r.json()['access_token']
        return access_token

    def get_jsapi_ticket(self, access_token):
        r = requests.get(url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=' + access_token +
                             '&type=jsapi')
        if r.json()['errcode'] == 0:
            jsapi_ticket = r.json()['ticket']
            return jsapi_ticket
        else:
            return -1

    def get_signature(self, jsapi_ticket, timestamp):
        noncestr = self.noncestr
        url = self.url

        if jsapi_ticket != -1:
            joint_string = 'jsapi_ticket=' + jsapi_ticket + '&noncestr=' + noncestr + '&timestamp=' + \
                           str(timestamp) + '&url=' + url

            signature = hashlib.sha1(joint_string).hexdigest()
            return signature

    def get_web_access_token(self, code):
        r = requests.get(
            url='https://api.weixin.qq.com/sns/oauth2/access_token?appid='+ self.appid +'&secret='+ self.appsecret +
                '&code='+ code +'&grant_type=authorization_code')
        return r.json()

    def get_user_info(self, access_token, openid):
        r = requests.get(
            url='https://api.weixin.qq.com/sns/userinfo?access_token='+ access_token +'&openid='+ openid +'&lang=zh_CN')
        return r.json()