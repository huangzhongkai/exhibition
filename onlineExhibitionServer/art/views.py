# -*- coding:utf8 -*-
import json, random, uuid
import time
from django.shortcuts import render_to_response, HttpResponse, Http404
from art.models import OeArtist, OeExhibit, OeExhibition, OeExhibitInterpretation,\
    OeArtistExhibitionRelation, OeWxConfig, OeWxDeveloper, OeExhibitionInterpretation, OeWxUser, OeUserExhibitionCollection
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from art.models import OeUser, OeExhibitComment, OeExhibitionComment, OeWxUserAttentionArtist, OeUserExhibitCollection
from django.contrib.sessions.models import Session

from art.utils import Wx
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from onlineExhibitionServer.settings import STATICFILES_DIRS
from django.utils.encoding import smart_unicode

from send_msg import send_sms
# Create your view here.


exhibits_list = [
        {
            'id': 0,
            'image_path': '/static/exhibit/朝奉图.jpeg',
            'name': '朝奉图',
            'author': '陈某',
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'image_text_readings': [
                {
                    'id': 0,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'id': 1,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                }
            ],
            'audio_readings': [
                {
                    'id': 0,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                },
                {
                    'id': 1,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                }
            ],
            'ratings': [
                {
                    "username": "张三",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                },
                {
                    "username": "李四",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                }
            ]
        },
        {
            'id': 1,
            'image_path': '/static/exhibit/树.jpeg',
            'name': '树',
            'author': '康某',
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'image_text_readings': [
                {
                    'id': 0,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'id': 1,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                }
            ],
            'audio_readings': [
                {
                    'id': 0,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                },
                {
                    'id': 1,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                }
            ],
            'ratings': [
                {
                    "username": "张三",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                },
                {
                    "username": "李四",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                }
            ]
        },
        {
            'id': 2,
            'image_path': '/static/exhibit/景.jpeg',
            'name': '景',
            'author': '大佬',
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'image_text_readings': [
                {
                    'id': 0,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'id': 1,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                }
            ],
            'audio_readings': [
                {
                    'id': 0,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                },
                {
                    'id': 1,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                }
            ],
            'ratings': [
                {
                    "username": "张三",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                },
                {
                    "username": "李四",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                }
            ]
        },
        {
            'id': 3,
            'image_path': '/static/exhibit/竹子.jpeg',
            'name': '竹子',
            'author': '小佬',
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'image_text_readings': [
                {
                    'id': 0,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'id': 1,
                    'image_path': '/static/exhibit/bamboo.jpeg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                }
            ],
            'audio_readings': [
                {
                    'id': 0,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                },
                {
                    'id': 1,
                    'play_icon': '/static/exhibit/play.svg',
                    'reading_title': '好看么',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                    'video_src': '/static/exhibit/test.mp4',
                    'audio_src': '/static/exhibit/lyg.mp3'
                }
            ],
            'ratings': [
                {
                    "username": "张三",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                },
                {
                    "username": "李四",
                    "rateTime": 1469281964000,
                    "text": "画的不错，非常赞；不亏是艺术大师的作品，值得大家学习学习",
                    "avatar": "http://static.galileo.xiaojukeji.com/static/tms/default_header.png",
                }
            ]
        },
    ]

exhibitions_list = [
    {
        'id': 0,
        'image_path': '/static/exhibition/head1.jpeg',
        'name': '陈小将极其盒子',
        'exhibition_date': '2017-7-4',
        'exhibition_site': '中国艺术馆',
        'exhibition_curator': '大佬',
        'audio_name': '中国建筑语音解读',
        'audio_src': '/static/exhibition/lyg.mp3',
        'image_text_readings': [
            {
                'id': 0,
                'image_path': '/static/exhibition/head1.jpeg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
                'id': 1,
                'image_path': '/static/exhibition/head2.jpeg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
        ],
        'audio_readings': [
            {
                'id': 0,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            },
            {
                'id': 1,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            }
        ],
        'charactors': [
            {
                'id': 0,
                'image_path': '/static/exhibit/朝奉图.jpeg'
            },
            {
                'id': 1,
                'image_path': '/static/exhibit/树.jpeg'
            }
        ],
        'enjoyables': [
            {
                'id': 2,
                'image_path': '/static/exhibit/景.jpeg'
            },
            {
                'id': 3,
                'image_path': '/static/exhibit/竹子.jpeg'
            }
        ]
    },
    {
        'id': 1,
        'image_path': '/static/exhibition/head2.jpeg',
        'name': '陈小将极其盒子1',
        'exhibition_date': '2017-7-4',
        'exhibition_site': '中国艺术馆',
        'exhibition_curator': '大佬',
        'audio_name': '中国建筑语音解读',
        'audio_src': '/static/exhibition/lyg.mp3',
        'image_text_readings': [
            {
                'id': 0,
                'image_path': '/static/exhibition/head1.jpeg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
                'id': 1,
                'image_path': '/static/exhibition/head2.jpeg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
        ],
        'audio_readings': [
            {
                'id': 0,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            },
            {
                'id': 1,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            }
        ],
        'charactors': [
            {
                'id': 0,
                'image_path': '/static/exhibit/朝奉图.jpeg'
            },
            {
                'id': 1,
                'image_path': '/static/exhibit/树.jpeg'
            }
        ],
        'enjoyables': [
            {
                'id': 2,
                'image_path': '/static/exhibit/景.jpeg'
            },
            {
                'id': 3,
                'image_path': '/static/exhibit/竹子.jpeg'
            }
        ]
    },
    {
        'id': 2,
        'image_path': '/static/exhibition/head3.jpeg',
        'name': '陈小将极其盒子2',
        'exhibition_date': '2017-7-4',
        'exhibition_site': '中国艺术馆',
        'exhibition_curator': '大佬',
        'audio_name': '中国建筑语音解读',
        'audio_src': '/static/exhibition/lyg.mp3',
        'image_text_readings': [
            {
                'id': 0,
                'image_path': '/static/exhibition/head1.jpeg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
                'id': 1,
                'image_path': '/static/exhibition/head2.jpeg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
        ],
        'audio_readings': [
            {
                'id': 0,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            },
            {
                'id': 1,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            }
        ],
        'charactors': [
            {
                'id': 0,
                'image_path': '/static/exhibit/朝奉图.jpeg'
            },
            {
                'id': 1,
                'image_path': '/static/exhibit/树.jpeg'
            }
        ],
        'enjoyables': [
            {
                'id': 2,
                'image_path': '/static/exhibit/景.jpeg'
            },
            {
                'id': 3,
                'image_path': '/static/exhibit/竹子.jpeg'
            }
        ]
    },
    {
        'id': 3,
        'image_path': '/static/exhibition/head4.jpeg',
        'name': '陈小将极其盒子3',
        'exhibition_date': '2017-7-4',
        'exhibition_site': '中国艺术馆',
        'exhibition_curator': '大佬',
        'audio_name': '中国建筑语音解读',
        'audio_src': '/static/exhibition/lyg.mp3',
        'image_text_readings': [
            {
                'id': 0,
                'image_path': '/static/exhibition/head1.jpeg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
                'id': 1,
                'image_path': '/static/exhibition/head2.jpeg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
        ],
        'audio_readings': [
            {
                'id': 0,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '我是来看展览的',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            },
            {
                'id': 1,
                'play_icon': '/static/exhibition/play.svg',
                'reading_title': '好看么',
                'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
                'video_src': '/static/exhibition/test.mp4',
                'audio_src': '/static/exhibition/lyg.mp3'
            }
        ],
        'charactors': [
            {
                'id': 0,
                'image_path': '/static/exhibit/朝奉图.jpeg'
            },
            {
                'id': 1,
                'image_path': '/static/exhibit/树.jpeg'
            }
        ],
        'enjoyables': [
            {
                'id': 2,
                'image_path': '/static/exhibit/景.jpeg'
            },
            {
                'id': 3,
                'image_path': '/static/exhibit/竹子.jpeg'
            }
        ]
    }
]


def artist(request, offset):
    code = request.GET.get('code', 'error')
    print request.COOKIES
    cookies = request.COOKIES

    artist = OeArtist.objects.filter(id=offset).first()
    artist = model_to_dict(artist)
    attention_count = OeWxUserAttentionArtist.objects.filter(artist=artist['id']).count()

    cookie = request.COOKIES.get('sessionid', 'error')
    if cookie != 'error':
        # openid = request.session.get('openid', default=None)
        try:
            openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            wx_user = OeWxUser.objects.filter(appid=openid).first().id
            if OeWxUserAttentionArtist.objects.filter(artist=artist['id'], wx_user=wx_user).count() > 0:
                isattention = 'true'
            else:
                isattention = 'false'
        except:
            isattention = 'false'
    else:
        isattention = 'false'
    artist_dict = {
        'id': artist['id'],
        'avatar': artist['head_path'],
        'name': artist['name'],
        'attention_count': attention_count,
        'isAttention': isattention
    }
    response = HttpResponse(json.dumps(artist_dict), content_type='application/json')

    if Session.objects.filter(session_key=cookies.get('sessionid','none')).first():
        return response

    if code != 'undefined' and code!= 'error':
        appid = OeWxDeveloper.objects.filter(id=1).first().appid
        appsecret = OeWxDeveloper.objects.filter(id=1).first().appsecret

        wx = Wx(appid, appsecret, '')
        access_token = wx.get_web_access_token(code)
        print access_token
        user_info = wx.get_user_info(access_token['access_token'], access_token['openid'])
        print user_info

        objs = Session.objects.all()
        for obj in objs:
            if obj.get_decoded().get('openid','') == user_info['openid']:
                response.set_cookie('sessionid', obj.session_key)
                print 'set cookie'
                return response
        request.session['openid'] =user_info['openid']
        nickname = user_info['nickname'].encode("ISO-8859-1").decode('utf-8')
        # OeUser.objects.create(nickname=user_info['nickname'].encode("ISO-8859-1").decode('utf-8'),
        #                       sex=user_info['sex'],
        #                       head_path=user_info['headimgurl'])
        OeWxUser.objects.create(appid=user_info['openid'],
                                nickname=user_info['nickname'].encode("ISO-8859-1").decode('utf-8'),
                                sex=str(user_info['sex']),
                                province=user_info['province'].encode("ISO-8859-1").decode('utf-8'),
                                city=user_info['city'].encode("ISO-8859-1").decode('utf-8'),
                                country=user_info['country'].encode("ISO-8859-1").decode('utf-8'),
                                headimgurl=user_info['headimgurl'])

        try:
            user_id = str(int(OeExhibitComment.objects.latest('create_time').id) + 1)
        except:
            user_id = '1'

        timeArray = time.localtime()
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        OeUser.objects.create(id=user_id,
                              nickname=user_info['nickname'].encode("ISO-8859-1").decode('utf-8'),
                              sex=str(user_info['sex']),
                              head_path=user_info['headimgurl'],
                              create_time=otherStyleTime)

        return response
    return response

def artists(request):
    artist_list = []

    artists = OeArtist.objects.all()
    for artist in artists:
        artist_dict = model_to_dict(artist)
        artist_dict['modify_time'] = artist_dict['modify_time'].strftime('%Y-%m-%d')
        artist_dict['create_time'] = artist_dict['create_time'].strftime('%Y-%m-%d')
        artist_list.append(artist_dict)
    print artist_list
    return HttpResponse(json.dumps(artist_list), content_type='application/json')

def exhibit(request, offset):
    print request.COOKIES
    print request.session.get('openid', default=None)
    # try:
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()

    #get exhibit base infomation
    exhibit = OeExhibit.objects.filter(id=offset).first()
    exhibit = model_to_dict(exhibit)

    #get exhibit image_text readings info
    image_text_reading_list = []
    image_text_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=0)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id':image_text_reading['id'],
            'image_path': image_text_reading['origin'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    # get exhibit audio reading info
    audio_reading_list = []
    audio_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=2)
    for audio_reading in audio_readings:
        audio_reading = model_to_dict(audio_reading)
        show_dict = {
            'id': audio_reading['id'],
            'reading_title': audio_reading['title'],
            'audio_src': audio_reading['origin'],
            'reading_content': audio_reading['content'],
        }
        audio_reading_list.append(show_dict)
    audio_reading_dict = {'audio_readings': audio_reading_list}

    #get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=1)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['origin'],
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'video_readings': video_reading_list}

    #get exhibit rating info
    comment_list = []
    comments = OeExhibitComment.objects.filter(exhibit__id=offset).order_by("create_time")
    for comment in comments:
        comment = model_to_dict(comment)
        wx_user = OeWxUser.objects.filter(id=comment['wx_user']).first()
        wx_user = model_to_dict(wx_user)

        if comment['parent'] != '' and comment['parent'] != None:
            parent_wx_user_id = OeExhibitComment.objects.filter(id=comment['parent']).first().wx_user_id
            parent_wx_user = OeWxUser.objects.filter(id=parent_wx_user_id).first()
            parent_wx_user = model_to_dict(parent_wx_user)
            text = smart_unicode('回复 ') + parent_wx_user['nickname'] + smart_unicode(' 的评论:') + comment['content']
        else:
            text = comment['content']
        show_dict = {
            'id': int(comment['id']),
            'username': wx_user['nickname'],
            'rateTime':  comment['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
            'text': text,
            'avatar': wx_user['headimgurl'],
            'wx_id':wx_user['id'],
            'type': comment['type'],
            'rate_image': comment['rate_image']
        }
        comment_list.append(show_dict)
    comment_dict = {'ratings': comment_list}

    cookie = request.COOKIES.get('sessionid', 'error')
    if cookie == 'error':
        return HttpResponse(json.dumps('error'), content_type='application/json')
    try:
        openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
        nickname = OeWxUser.objects.filter(appid=openid).first().nickname
    except:
        openid = ''
        nickname = ''
    user = OeUser.objects.filter(nickname=nickname).first()
    if OeUserExhibitCollection.objects.filter(user=user.id, exhibit=offset).first():
        collect_flag = True
    else:
        collect_flag = False

    exhibit_dict = {
        'id': offset,
        'image_path': exhibit['image_path'],
        'name': exhibit['name'],
        'author': exhibit['author'],
        'audio_name': '作品解读',
        'audio_src': '/static/exhibit/lyg.mp3',
        'collect_flag': collect_flag
    }

    exhibit_dict = dict(exhibit_dict, **image_text_reading_dict)
    exhibit_dict = dict(exhibit_dict, **audio_reading_dict)
    exhibit_dict = dict(exhibit_dict, **video_reading_dict)
    exhibit_dict = dict(exhibit_dict, **comment_dict)

    return HttpResponse(json.dumps(exhibit_dict), content_type='application/json')

def exhibits(request):
    print request.COOKIES
    exhibit_l=[]
    exhibition = request.GET.get('exhibition', 'error')
    artist_id = request.GET.get('artist', 'error')
    if exhibition != 'error':
        type = request.GET.get('type', 'error')
        if type == 'charactor':
            exhibits = OeExhibit.objects.filter(exhibition__id=exhibition, category__id=0)
            for exhibit in exhibits:
                exhibit_l.append(model_to_dict(exhibit))
        elif type == 'enjoyable':
            exhibits = OeExhibit.objects.filter(exhibition__id=exhibition, category__id=1)
            for exhibit in exhibits:
                exhibit_l.append(model_to_dict(exhibit))
        return HttpResponse(json.dumps(exhibit_l), content_type='application/json')

    if artist_id != 'error':
        artist = OeArtist.objects.filter(id=artist_id).first()
        exhibits = OeExhibit.objects.filter(author=artist.name)
        for exhibit in exhibits:
            exhibit = model_to_dict(exhibit)
            show_dict = {
                'id': exhibit['id'],
                'image_path':exhibit['image_path'],
                'name': exhibit['name'],
                'author': exhibit['author']
            }
            exhibit_l.append(show_dict)
    return HttpResponse(json.dumps(exhibit_l), content_type='application/json')

def exhibit_readings(request, offset):
    print request.COOKIES
    # get exhibit image_text readings info
    image_text_reading_list = []
    image_text_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=0)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id': image_text_reading['id'],
            'image_path': image_text_reading['origin'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    # get exhibit audio reading info
    audio_reading_list = []
    audio_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=2)
    for audio_reading in audio_readings:
        audio_reading = model_to_dict(audio_reading)
        show_dict = {
            'id': audio_reading['id'],
            'reading_title': audio_reading['title'],
            'audio_src': audio_reading['origin'],
            'reading_content': audio_reading['content'],
        }
        audio_reading_list.append(show_dict)
    audio_reading_dict = {'audio_readings': audio_reading_list}

    # get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitInterpretation.objects.filter(exhibit__id=offset, type=1)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['origin'],
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'video_readings': video_reading_list}

    reading_dict = {}
    reading_dict = dict(reading_dict, **image_text_reading_dict)
    reading_dict = dict(reading_dict, **audio_reading_dict)
    reading_dict = dict(reading_dict, **video_reading_dict)


    return HttpResponse(json.dumps(reading_dict), content_type='application/json')

@csrf_exempt
def exhibit_ratings(request, offset):
    if request.method == 'POST':
        print request.COOKIES
        print request.session.get('openid', default=None)

        cookie = request.COOKIES.get('sessionid','error')
        if cookie != 'error':
            try:
                openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            except:
                openid = ''
            # openid = request.session.get('openid', default=None)
            nickname = OeWxUser.objects.filter(appid=openid).first().nickname
        else:
            print '未知'
            nickname = '未知'
        timeArray = time.localtime()

        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


        rating = {}
        # if not OeUser.objects.filter(user_name=request.POST.get('username', '')).first():
        #     user = {
        #         'user_name': request.POST.get('username', ''),
        #         'head_path': request.POST.get('avatar', ''),
        #         'create_time': otherStyleTime,
        #         'id': str(int(OeUser.objects.latest('id').id) + 1)
        #     }
        #     OeUser.objects.create(**user)
        #     rating['user'] = OeUser.objects.filter(id=str(OeUser.objects.all().count() - 1)).first()
        # else:
        #     rating['user'] = OeUser.objects.filter(user_name=request.POST.get('username', '')).first()

        # rating['user'] = OeUser.objects.filter().first()

        rating['wx_user'] = OeWxUser.objects.filter(nickname=nickname).first()
        rating['exhibit'] = OeExhibit.objects.filter(id=offset).first()
        rating['create_time'] = otherStyleTime

        parent_id = request.POST.get('parent_id', '')
        if parent_id == '-1':
            rating['content'] = request.POST.get('text', '')
        else:
            rating['content'] = request.POST.get('text', '')
            rating['parent'] = OeExhibitComment.objects.filter(id=parent_id).first()
        try:
            rating['id'] = str(int(OeExhibitComment.objects.latest('create_time').id) + 1)
        except:
            rating['id'] = '1'
        if cookie == 'error':
            return HttpResponse(json.dumps('error'), content_type='application/json')
        if request.GET.get('type','') == '1':
            image = request.FILES.get('imageblob')
            path = default_storage.save(STATICFILES_DIRS[0] + '/exhibit/image_rating/' + image.name + otherStyleTime +'.jpeg', ContentFile(image.read()))
        if request.GET.get('type','') == '1':
            rating['type'] = 1
            rating['rate_image'] = '/static/exhibit/image_rating/' + image.name + otherStyleTime + '.jpeg'
        else:
            rating['type'] = 0
        OeExhibitComment.objects.create(**rating)


        return HttpResponse(json.dumps(''), content_type='application/json')

@csrf_exempt
def exhibition(request, offset):
    if request.method == 'GET':
        print request.COOKIES
        # get exhibition base infomation
        exhibition = OeExhibition.objects.filter(id=offset).first()
        exhibition = model_to_dict(exhibition)

        # get exhibition image_text readings info
        image_text_reading_list = []
        image_text_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=0)
        for image_text_reading in image_text_readings:
            image_text_reading = model_to_dict(image_text_reading)
            show_dict = {
                'id': image_text_reading['id'],
                'image_path': image_text_reading['origin'],
                'reading_title': image_text_reading['title'],
                'reading_content': image_text_reading['content'],
            }
            image_text_reading_list.append(show_dict)
        image_text_reading_dict = {'image_text_readings': image_text_reading_list}

        #get exhibition audio reading info
        audio_reading_list = []
        audio_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=2)
        for audio_reading in audio_readings:
            audio_reading = model_to_dict(audio_reading)
            show_dict = {
                'id': audio_reading['id'],
                'reading_title': audio_reading['title'],
                'audio_src': audio_reading['origin'],
                'reading_content': audio_reading['content'],
            }
            audio_reading_list.append(show_dict)
        audio_reading_dict = {'audio_readings': audio_reading_list}


        # get exhibition video reading info
        video_reading_list = []
        video_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=1)
        for video_reading in video_readings:
            video_reading = model_to_dict(video_reading)
            show_dict = {
                'id': video_reading['id'],
                'reading_title': video_reading['title'],
                'reading_content': video_reading['content'],
                'video_src': video_reading['origin'],
                # 'play_icon': video_reading['play_icon']
            }
            video_reading_list.append(show_dict)
        video_reading_dict = {'video_readings': video_reading_list}

        # get exhibit rating info
        comment_list = []
        comments = OeExhibitionComment.objects.filter(exhibition__id=offset).order_by("create_time")
        for comment in comments:
            comment = model_to_dict(comment)
            wx_user = OeWxUser.objects.filter(id=comment['wx_user']).first()
            wx_user = model_to_dict(wx_user)

            if comment['parent'] != '' and comment['parent'] != None:
                parent_wx_user_id = OeExhibitionComment.objects.filter(id=comment['parent']).first().wx_user_id
                parent_wx_user = OeWxUser.objects.filter(id=parent_wx_user_id).first()
                parent_wx_user = model_to_dict(parent_wx_user)
                text = smart_unicode('回复 ') + parent_wx_user['nickname'] + smart_unicode(' 的评论:') + comment['content']
            else:
                text = comment['content']
            show_dict = {
                'id': int(comment['id']),
                'username': wx_user['nickname'],
                'rateTime': comment['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
                'text': text,
                'avatar': wx_user['headimgurl'],
                'wx_id': wx_user['id'],
                'type': comment['type'],
                'rate_image': comment['rate_image']
            }
            comment_list.append(show_dict)
        comment_dict = {'ratings': comment_list}

        #get charactor exhibit
        charactor_list = []
        charactors = OeExhibit.objects.filter(category__id=0, exhibition_id=offset)
        for charactor in charactors:
            charactor = model_to_dict(charactor)
            show_dict = {
                'id': charactor['id'],
                'image_path': charactor['image_path']
            }
            charactor_list.append(show_dict)
        charactor_dict = {'charactors': charactor_list}

        #get enjoyable exhibit
        enjoyable_list = []
        enjoyables = OeExhibit.objects.filter(category__id=1, exhibition_id=offset)
        for enjoyable in enjoyables:
            enjoyable = model_to_dict(enjoyable)
            show_dict = {
                'id': enjoyable['id'],
                'image_path': enjoyable['image_path']
            }
            enjoyable_list.append(show_dict)
        enjoyable_dict = {'enjoyables': enjoyable_list}

        cookie = request.COOKIES.get('sessionid', 'error')
        if cookie == 'error':
            return HttpResponse(json.dumps('error'), content_type='application/json')
        try:
            openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            nickname = OeWxUser.objects.filter(appid=openid).first().nickname
        except:
            openid = ''
            nickname = ''
        user = OeUser.objects.filter(nickname=nickname).first()
        if OeUserExhibitionCollection.objects.filter(user=user.id, exhibition=offset).first():
            collect_flag = True
        else:
            collect_flag = False

        exhibition_dict = {
            'id': offset,
            'image_path': exhibition['image_path'],
            'name': exhibition['name'],
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'exhibition_date': '2017-7-4',
            'exhibition_site': '中国艺术馆',
            'exhibition_curator': '大佬',
            'collect_flag': collect_flag
        }

        exhibition_dict = dict(exhibition_dict, **image_text_reading_dict)
        exhibition_dict = dict(exhibition_dict, **audio_reading_dict)
        exhibition_dict = dict(exhibition_dict, **video_reading_dict)
        exhibition_dict = dict(exhibition_dict, **comment_dict)
        exhibition_dict = dict(exhibition_dict, **charactor_dict)
        exhibition_dict = dict(exhibition_dict, **enjoyable_dict)
        return HttpResponse(json.dumps(exhibition_dict), content_type='application/json')


def exhibitions(request):
    print request.COOKIES
    exhibition_l = []
    exhibition_id_list = []
    artist = request.GET.get('artist', '0')
    try:
        artist = int(artist)
    except ValueError:
        raise Http404()

    exhibition_set = OeArtistExhibitionRelation.objects.filter(artist=artist)
    for exhibition in exhibition_set:
        exhibition_id_list.append(exhibition.exhibiton_id)
    exhibitions = OeExhibition.objects.filter(id__in=exhibition_id_list)
    for exhibition in exhibitions:
        exhibition = model_to_dict(exhibition)

        exhibition_dict = {
            'id': exhibition['id'],
            'image_path': exhibition['image_path'],
            'name': exhibition['name'],
            'exhibition_date': '2017-7-4',
            'exhibition_site': '中国艺术馆',
            'exhibition_curator': '大佬',
        }
        exhibition_l.append(exhibition_dict)

    return HttpResponse(json.dumps(exhibition_l), content_type='application/json')


def exhibition_readings(request, offset):
    # get exhibit image_text readings info
    image_text_reading_list = []
    image_text_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=0)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id': image_text_reading['id'],
            'image_path': image_text_reading['origin'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    # get exhibition audio reading info
    audio_reading_list = []
    audio_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=2)
    for audio_reading in audio_readings:
        audio_reading = model_to_dict(audio_reading)
        show_dict = {
            'id': audio_reading['id'],
            'reading_title': audio_reading['title'],
            'audio_src': audio_reading['origin'],
            'reading_content': audio_reading['content'],
        }
        audio_reading_list.append(show_dict)
    audio_reading_dict = {'audio_readings': audio_reading_list}

    # get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitionInterpretation.objects.filter(exhibition__id=offset, type=1)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['origin'],
            # 'play_icon': video_reading['play_icon']
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'video_readings': video_reading_list}

    reading_dict = {}
    reading_dict = dict(reading_dict, **image_text_reading_dict)
    reading_dict = dict(reading_dict, **audio_reading_dict)
    reading_dict = dict(reading_dict, **video_reading_dict)

    return HttpResponse(json.dumps(reading_dict), content_type='application/json')

def exhibit_image_text_readings(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibit_reading = OeExhibitInterpretation.objects.filter(id=offset).first()
    exhibit_reading = model_to_dict(exhibit_reading)

    exhibit = OeExhibit.objects.filter(id=exhibit_reading['exhibit']).first()
    exhibit = model_to_dict(exhibit)

    image_text_readings = {
        'id': exhibit_reading['id'],
        'title':exhibit['name'],
        'image_path': exhibit_reading['origin'],
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'.split('。')
    }

    return HttpResponse(json.dumps(image_text_readings), content_type='application/json')


def exhibit_vedio_readings(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibit_reading = OeExhibitInterpretation.objects.filter(id=offset).first()
    exhibit_reading = model_to_dict(exhibit_reading)

    video_readings = {
        'id': exhibit_reading['id'],
        'video_src': exhibit_reading['origin'],
        'poster':'/static/exhibition/head1.jpeg',
        'reading_content':'张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
      一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
      他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
      重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
      名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
      黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'.split('。')
    }
    return HttpResponse(json.dumps(video_readings), content_type='application/json')

@csrf_exempt
def exhibition_ratings(request, offset):
    if request.method == 'POST':
        print request.COOKIES
        print request.session.get('openid', default=None)

        cookie = request.COOKIES.get('sessionid','error')
        if cookie != 'error':
            try:
                openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            except:
                openid = ''
            # openid = request.session.get('openid', default=None)
            nickname = OeWxUser.objects.filter(appid=openid).first().nickname
        else:
            print '未知'
            nickname = '未知'
        timeArray = time.localtime()

        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


        rating = {}
        # if not OeUser.objects.filter(user_name=request.POST.get('username', '')).first():
        #     user = {
        #         'user_name': request.POST.get('username', ''),
        #         'head_path': request.POST.get('avatar', ''),
        #         'create_time': otherStyleTime,
        #         'id': str(int(OeUser.objects.latest('id').id) + 1)
        #     }
        #     OeUser.objects.create(**user)
        #     rating['user'] = OeUser.objects.filter(id=str(OeUser.objects.all().count() - 1)).first()
        # else:
        #     rating['user'] = OeUser.objects.filter(user_name=request.POST.get('username', '')).first()

        # rating['user'] = OeUser.objects.filter().first()

        rating['wx_user'] = OeWxUser.objects.filter(nickname=nickname).first()
        rating['exhibition'] = OeExhibition.objects.filter(id=offset).first()
        rating['create_time'] = otherStyleTime

        parent_id = request.POST.get('parent_id', '')
        if parent_id == '-1':
            rating['content'] = request.POST.get('text', '')
        else:
            rating['content'] = request.POST.get('text', '')
            rating['parent'] = OeExhibitionComment.objects.filter(id=parent_id).first()
        try:
            rating['id'] = str(int(OeExhibitionComment.objects.latest('create_time').id) + 1)
        except:
            rating['id'] = '1'
        if cookie == 'error':
            return HttpResponse(json.dumps('error'), content_type='application/json')
        if request.GET.get('type','') == '1':
            image = request.FILES.get('imageblob')
            path = default_storage.save(STATICFILES_DIRS[0] + '/exhibit/image_rating/' + image.name + otherStyleTime +'.jpeg', ContentFile(image.read()))
        if request.GET.get('type','') == '1':
            rating['type'] = 1
            rating['rate_image'] = '/static/exhibit/image_rating/' + image.name + otherStyleTime + '.jpeg'
        else:
            rating['type'] = 0
        print rating
        OeExhibitionComment.objects.create(**rating)

        return HttpResponse(json.dumps(''), content_type='application/json')


def exhibition_image_text_readings(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibition_reading = OeExhibitionInterpretation.objects.filter(id=offset).first()
    exhibition_reading = model_to_dict(exhibition_reading)

    image_text_readings = {
        'id': exhibition_reading['id'],
        'image_path': exhibition_reading['origin'],
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'.split('。')
    }

    return HttpResponse(json.dumps(image_text_readings), content_type='application/json')


def exhibition_vedio_readings(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibition_reading = OeExhibitionInterpretation.objects.filter(id=offset).first()
    exhibition_reading = model_to_dict(exhibition_reading)

    video_readings = {
        'id': exhibition_reading['id'],
        'video_src': exhibition_reading['origin'],
        'poster': '/static/exhibition/head1.jpeg',
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'.split('。')
    }
    return HttpResponse(json.dumps(video_readings), content_type='application/json')

@csrf_exempt
def attention(request):
    print request.COOKIES
    print request.session.get('openid', default=None)
    cookie = request.COOKIES.get('sessionid', 'error')
    if cookie == 'error':
        return HttpResponse(json.dumps('error'), content_type='application/json')
    openid = request.session.get('openid', default=None)
    wx_user = OeWxUser.objects.filter(appid=openid).first()
    if request.method == 'POST':
        artist_id = request.GET.get('artist_id', '0')
        artist = OeArtist.objects.filter(id=artist_id).first()
        OeWxUserAttentionArtist.objects.create(wx_user=wx_user, artist=artist)
        return HttpResponse(json.dumps({}), content_type='application/json')
    if request.method == 'DELETE':
        artist_id = request.GET.get('artist_id', '0')
        artist = OeArtist.objects.filter(id=artist_id).first()
        OeWxUserAttentionArtist.objects.filter(wx_user=wx_user, artist=artist).delete()
        return HttpResponse(json.dumps({}), content_type='application/json')
#
def introduction(request):
    artist = request.GET.get('artist', '0')
    try:
        artist = int(artist)
    except ValueError:
        raise Http404()
    introduction = OeArtist.objects.filter(id=artist).first()
    introduction_dict = model_to_dict(introduction)
    introduction_list = introduction_dict['intro'].split(';')
    return HttpResponse(json.dumps(introduction_list), content_type='application/json')

def achievement(request):
    artist = request.GET.get('artist', '0')
    try:
        artist = int(artist)
    except ValueError:
        raise Http404()
    achievement = OeArtist.objects.filter(id=artist).first()
    achievement_dict = model_to_dict(achievement)

    achievement_list = achievement_dict['achievement'].split(';')
    return HttpResponse(json.dumps(achievement_list), content_type='application/json')

def information(request,offset):
    if request.method == "GET":
        wxUser = OeWxUser.objects.filter(id=int(offset)).first()
        wxUser = model_to_dict(wxUser)

        wx_user_nickname = OeWxUser.objects.filter(id=int(offset)).first().nickname
        mobile_phone = OeUser.objects.filter(nickname=wx_user_nickname).first().mobile_phone
        person_dict = {
            'id': wxUser['id'],
            'avatar': wxUser['headimgurl'],
            'name': wxUser['nickname'],
            'phone_number':mobile_phone
        }
        response = HttpResponse(json.dumps(person_dict), content_type='application/json')
        return response

@csrf_exempt
def collect(request, offset):
    if request.method == "GET":
        print offset
        wx_user_nickname = OeWxUser.objects.filter(id=int(offset)).first().nickname
        user_id = OeUser.objects.filter(nickname=wx_user_nickname).first().id

        exhibit_collect_list = []
        exhibit_collects = OeUserExhibitCollection.objects.filter(user=user_id)
        for exhibit_collect in exhibit_collects:
            exhibit_collect = model_to_dict(exhibit_collect)
            exhibit = OeExhibit.objects.filter(id=exhibit_collect['exhibit']).first()
            exhibit = model_to_dict(exhibit)
            collect_dict = {
                'flag':'flag' + exhibit['id'],
                'id': exhibit['id'],
                'image_path': exhibit['image_path'],
                'name': exhibit['name'],
                'author': exhibit['author'],
            }
            exhibit_collect_list.append(collect_dict)

        exhibition_collect_list = []
        exhibition_collects = OeUserExhibitionCollection.objects.filter(user=user_id)
        for exhibition_collect in exhibition_collects:
            exhibition_collect = model_to_dict(exhibition_collect)
            exhibition = OeExhibition.objects.filter(id=exhibition_collect['exhibition']).first()
            exhibition = model_to_dict(exhibition)
            collect_dict = {
                'flag': '_flag' + exhibition['id'],
                'id': exhibition['id'],
                'image_path': exhibition['image_path'],
                'name': exhibition['name'],
                'exhibition_date': '2017-7-4',
                'exhibition_site': '中国艺术馆',
                'exhibition_curator': '大佬',
            }
            exhibition_collect_list.append(collect_dict)
        return_collect_dict = {
            'exhibits':exhibit_collect_list,
            'exhibitions': exhibition_collect_list
        }

        response = HttpResponse(json.dumps(return_collect_dict), content_type='application/json')
        return response
    if request.method == "POST":
        cookie = request.COOKIES.get('sessionid', 'error')
        if cookie == 'error':
            return HttpResponse(json.dumps('error'), content_type='application/json')

        try:
            openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            nickname = OeWxUser.objects.filter(appid=openid).first().nickname
        except:
            openid = ''
            nickname = ''
        if request.GET.get('type') == '0':
            user = OeUser.objects.filter(nickname=nickname).first()
            exhibit = OeExhibit.objects.filter(id=offset).first()
            try:
                collection_id = str(int(OeUserExhibitCollection.objects.latest('id').id) + 1)
            except:
                collection_id = '1'
            if not OeUserExhibitCollection.objects.filter(user=user,exhibit=exhibit).first():
                OeUserExhibitCollection.objects.create(id=collection_id,
                                                       user=user,
                                                       exhibit=exhibit)
        if request.GET.get('type') == '1':
            user = OeUser.objects.filter(nickname=nickname).first()
            exhibition = OeExhibition.objects.filter(id=offset).first()
            try:
                collection_id = str(int(OeUserExhibitionCollection.objects.latest('id').id) + 1)
            except:
                collection_id = '1'
            if not OeUserExhibitionCollection.objects.filter(user=user, exhibition=exhibition).first():
                OeUserExhibitionCollection.objects.create(id=collection_id,
                                                          user=user,
                                                          exhibition=exhibition)

        response = HttpResponse(json.dumps({}), content_type='application/json')
        return response
    if request.method == "DELETE":
        cookie = request.COOKIES.get('sessionid', 'error')
        if cookie == 'error':
            return HttpResponse(json.dumps('error'), content_type='application/json')

        try:
            openid = Session.objects.get(session_key=cookie).get_decoded()['openid']
            nickname = OeWxUser.objects.filter(appid=openid).first().nickname
        except:
            openid = ''
            nickname = ''
        print request.GET.get('type')
        if request.GET.get('type') == '0':
            user = OeUser.objects.filter(nickname=nickname).first()
            OeUserExhibitCollection.objects.filter(user=user.id, exhibit=offset).delete()
        if request.GET.get('type') == '1':
            user = OeUser.objects.filter(nickname=nickname).first()
            OeUserExhibitionCollection.objects.filter(user=user.id, exhibition=offset).delete()

        response = HttpResponse(json.dumps({}), content_type='application/json')
        return response

@csrf_exempt
def send_auth_code(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number', '')
        wx_user_id = request.POST.get('wx_user_id', '')
        __business_id = uuid.uuid1()
        print __business_id
        code = str(random.randrange(100000, 999999, 6))
        params = {"code":code}
        result = send_sms(__business_id, phone_number, "艺术展厅app", "SMS_91030041", json.dumps(params))

        if json.loads(result)['Message'] == 'OK':
            return_dict = {'code': 200}
            OeWxUser.objects.filter(id=int(wx_user_id)).update(auth_code=code, bind_phone=phone_number)
        else:
            return_dict = {'code': -1}
        response = HttpResponse(json.dumps(return_dict), content_type='application/json')
        return response

@csrf_exempt
def bing_phone_commit(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number', '')
        auth_code = request.POST.get('auth_code', '')
        wx_user_id = request.POST.get('wx_user_id', '')

        if OeWxUser.objects.filter(id=int(wx_user_id), auth_code=auth_code, bind_phone=phone_number):
            wx_user_nickname = OeWxUser.objects.filter(id=int(wx_user_id)).first().nickname
            OeUser.objects.filter(nickname=wx_user_nickname).update(mobile_phone=phone_number)
            return_dict = {'code': 200}
        else:
            return_dict = {'code': -1}
        response = HttpResponse(json.dumps(return_dict), content_type='application/json')
        return response

def artist_html(request):
    return render_to_response('artist.html', locals())

def exhibit_html(request):
    return render_to_response('exhibit.html', locals())

def exhibition_html(request):
    return render_to_response('exhibition.html', locals())

def home_html(request):
    return render_to_response('home.html', locals())

def video_readings_html(request):
    return render_to_response('video_readings.html', locals())

def image_text_readings_html(request):
    return render_to_response('image_text_readings.html', locals())

def personal_information_html(request):
    return render_to_response('information.html', locals())


def motified_signature(request):
    if request.method == 'GET':
        url = request.GET.get('url', '0').decode('utf-8')
        appid = OeWxDeveloper.objects.filter(id=1).first().appid
        appsecret = OeWxDeveloper.objects.filter(id=1).first().appsecret

        wx = Wx(appid, appsecret, url)
        developer = OeWxDeveloper.objects.filter(id=1).first()
        if developer.jsapi_ticket and time.time() - developer.create_timestamp < 7200:
            print  'use old jsapi_ticket'
            timestamp = int(time.time())
            signature = wx.get_signature(developer.jsapi_ticket, timestamp)
        else:
            print 'modified developer info'
            access_token = wx.get_access_token()
            jsapi_ticket = wx.get_jsapi_ticket(access_token)
            timestamp = int(time.time())
            signature = wx.get_signature(jsapi_ticket, timestamp)
            OeWxDeveloper.objects.filter(id=1).update(access_token=access_token,
                                                      jsapi_ticket=jsapi_ticket,
                                                      create_timestamp=timestamp)
        return_dict = {
            'appid': appid,
            'appsecret': appsecret,
            'url': url,
            'timestamp': timestamp,
            'noncestr': wx.noncestr,
            'signature': signature
        }
        OeWxConfig.objects.filter(url=url).update(**return_dict)
        return HttpResponse(json.dumps({}), content_type='application/json')


def get_signature(request):

    if request.method == 'GET':
        url = request.GET.get('url', '0').decode('utf-8')

        # if url.find('&code=') != -1:
        #     code = url.split('&code=')[1].split('&')[0]

        appid = OeWxDeveloper.objects.filter(id=1).first().appid
        appsecret = OeWxDeveloper.objects.filter(id=1).first().appsecret

        config = OeWxConfig.objects.filter(url=url, appid=appid, appsecret=appsecret).first()
        if config:
            return_dict = {
                'appid':config.appid,
                'timestamp': config.timestamp,
                'noncestr': config.noncestr,
                'signature': config.signature
            }
            return HttpResponse(json.dumps(return_dict), content_type='application/json')
        else:
            wx = Wx(appid, appsecret, url)
            developer = OeWxDeveloper.objects.filter(id=1).first()
            if developer.jsapi_ticket and time.time() - developer.create_timestamp < 7200:
                print  'use old jsapi_ticket'
                timestamp = int(time.time())
                signature = wx.get_signature(developer.jsapi_ticket, timestamp)
            else:
                print 'modified developer info'
                access_token = wx.get_access_token()
                jsapi_ticket = wx.get_jsapi_ticket(access_token)
                timestamp = int(time.time())
                signature = wx.get_signature(jsapi_ticket, timestamp)
                OeWxDeveloper.objects.filter(id=1).update(access_token=access_token,
                                                          jsapi_ticket=jsapi_ticket,
                                                          create_timestamp=timestamp)
            return_dict = {
                'appid': appid,
                'appsecret': appsecret,
                'url': url,
                'timestamp': timestamp,
                'noncestr': wx.noncestr,
                'signature': signature
            }
            OeWxConfig.objects.create(**return_dict)

            config = OeWxConfig.objects.filter(url=url, appid=appid, appsecret=appsecret).first()
            return_dict = {
                'appid': config.appid,
                'timestamp': config.timestamp,
                'noncestr': config.noncestr,
                'signature': config.signature
            }
            return HttpResponse(json.dumps(return_dict), content_type='application/json')
