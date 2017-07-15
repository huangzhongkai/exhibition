# -*- coding:utf8 -*-
import json
import datetime,time
from django.shortcuts import render_to_response, HttpResponse, Http404
from art.models import OeArtist, OeExhibit, OeExhibition, OeExhibitionImageTextReading,OeExhibitionVideoReading, \
    OeArtistExhibitionRelation, OeWxConfig
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from art.models import OeExhibitImageTextReading, OeExhibitVideoReading, OeUser, OeExhibitComment, OeExhibitionComment

import hashlib
import requests
from art.utils import Wx
# Create your views here.


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
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    artist = OeArtist.objects.filter(id=offset).first()
    artist = model_to_dict(artist)
    # artist_dict['modify_time'] = artist_dict['modify_time'].strftime('%Y-%m-%d')
    # artist_dict['create_time'] = artist_dict['create_time'].strftime('%Y-%m-%d')
    artist_dict = {
        'avatar': artist['head_path'],
        'name': artist['name'],
        'attention_count': 200
    }
    return HttpResponse(json.dumps(artist_dict), content_type='application/json')

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
    print 'offset=', offset
    # try:
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()

    #get exhibit base infomation
    exhibit = OeExhibit.objects.filter(id=offset).first()
    exhibit = model_to_dict(exhibit)

    #get exhibit image_text readings info
    image_text_reading_list = []
    image_text_readings = OeExhibitImageTextReading.objects.filter(exhibit__id=offset)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id':image_text_reading['id'],
            'image_path': image_text_reading['image_path'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    #get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitVideoReading.objects.filter(exhibit__id=offset)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['video_path'],
            'play_icon': video_reading['play_icon']
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'audio_readings': video_reading_list}

    #get exhibit rating info
    comment_list = []
    comments = OeExhibitComment.objects.filter(exhibit__id=offset)
    for comment in comments:
        comment = model_to_dict(comment)
        user = OeUser.objects.filter(id=comment['user']).first()
        user = model_to_dict(user)
        show_dict = {
            'username': user['user_name'],
            'rateTime':  comment['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
            'text': comment['content'],
            'avatar': user['head_path']
        }
        comment_list.append(show_dict)
    comment_dict = {'ratings': comment_list}

    exhibit_dict = {
        'id': offset,
        'image_path': exhibit['image_path'],
        'name': exhibit['name'],
        'author': exhibit['author'],
        'audio_name': '作品解读',
        'audio_src': '/static/exhibit/lyg.mp3',
    }

    exhibit_dict = dict(exhibit_dict, **image_text_reading_dict)
    exhibit_dict = dict(exhibit_dict, **video_reading_dict)
    exhibit_dict = dict(exhibit_dict, **comment_dict)

    return HttpResponse(json.dumps(exhibit_dict), content_type='application/json')

def exhibits(request):
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
        print exhibits
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

    # get exhibit image_text readings info
    image_text_reading_list = []
    image_text_readings = OeExhibitImageTextReading.objects.filter(exhibit__id=offset)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id': image_text_reading['id'],
            'image_path': image_text_reading['image_path'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    # get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitVideoReading.objects.filter(exhibit__id=offset)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['video_path'],
            'play_icon': video_reading['play_icon']
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'audio_readings': video_reading_list}

    reading_dict = {}
    reading_dict = dict(reading_dict, **image_text_reading_dict)
    reading_dict = dict(reading_dict, **video_reading_dict)


    return HttpResponse(json.dumps(reading_dict), content_type='application/json')

@csrf_exempt
def exhibit_ratings(request, offset):
    if request.method == 'POST':
        timeArray = time.localtime()
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        rating = {}
        if not OeUser.objects.filter(user_name=request.POST.get('username', '')).first():
            user = {
                'user_name': request.POST.get('username', ''),
                'head_path': request.POST.get('avatar', ''),
                'create_time': otherStyleTime,
                'id': str(int(OeUser.objects.latest('id').id) + 1)
            }
            OeUser.objects.create(**user)
            rating['user'] = OeUser.objects.filter(id=str(OeUser.objects.all().count() - 1)).first()
        else:
            rating['user'] = OeUser.objects.filter(user_name=request.POST.get('username', '')).first()

        rating['exhibit'] = OeExhibit.objects.filter(id=offset).first()
        rating['create_time'] = otherStyleTime
        rating['content'] = request.POST.get('text', '')
        rating['id'] = str(int(OeExhibitComment.objects.latest('id').id) + 1)

        OeExhibitComment.objects.create(**rating)


        return HttpResponse(json.dumps(''), content_type='application/json')

@csrf_exempt
def exhibition(request, offset):
    if request.method == 'GET':

        # get exhibition base infomation
        exhibition = OeExhibition.objects.filter(id=offset).first()
        exhibition = model_to_dict(exhibition)

        # get exhibit image_text readings info
        image_text_reading_list = []
        image_text_readings = OeExhibitionImageTextReading.objects.filter(exhibition__id=offset)
        for image_text_reading in image_text_readings:
            image_text_reading = model_to_dict(image_text_reading)
            show_dict = {
                'id': image_text_reading['id'],
                'image_path': image_text_reading['image_path'],
                'reading_title': image_text_reading['title'],
                'reading_content': image_text_reading['content'],
            }
            image_text_reading_list.append(show_dict)
        image_text_reading_dict = {'image_text_readings': image_text_reading_list}

        # get exhibit video reading info
        video_reading_list = []
        video_readings = OeExhibitionVideoReading.objects.filter(exhibition__id=offset)
        for video_reading in video_readings:
            video_reading = model_to_dict(video_reading)
            show_dict = {
                'id': video_reading['id'],
                'reading_title': video_reading['title'],
                'reading_content': video_reading['content'],
                'video_src': video_reading['video_path'],
                'play_icon': video_reading['play_icon']
            }
            video_reading_list.append(show_dict)
        video_reading_dict = {'audio_readings': video_reading_list}

        # get exhibit rating info
        comment_list = []
        comments = OeExhibitionComment.objects.filter(exhibition__id=offset)
        for comment in comments:
            comment = model_to_dict(comment)
            user = OeUser.objects.filter(id=comment['user']).first()
            user = model_to_dict(user)
            show_dict = {
                'username': user['user_name'],
                'rateTime': comment['create_time'].strftime('%Y-%m-%d %H:%M:%S'),
                'text': comment['content'],
                'avatar': user['head_path']
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

        exhibition_dict = {
            'id': offset,
            'image_path': exhibition['image_path'],
            'name': exhibition['name'],
            'audio_name': '作品解读',
            'audio_src': '/static/exhibit/lyg.mp3',
            'exhibition_date': '2017-7-4',
            'exhibition_site': '中国艺术馆',
            'exhibition_curator': '大佬',
        }

        exhibition_dict = dict(exhibition_dict, **image_text_reading_dict)
        exhibition_dict = dict(exhibition_dict, **video_reading_dict)
        exhibition_dict = dict(exhibition_dict, **comment_dict)
        exhibition_dict = dict(exhibition_dict, **charactor_dict)
        exhibition_dict = dict(exhibition_dict, **enjoyable_dict)
        return HttpResponse(json.dumps(exhibition_dict), content_type='application/json')


def exhibitions(request):
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
    image_text_readings = OeExhibitionImageTextReading.objects.filter(exhibition__id=offset)
    for image_text_reading in image_text_readings:
        image_text_reading = model_to_dict(image_text_reading)
        show_dict = {
            'id': image_text_reading['id'],
            'image_path': image_text_reading['image_path'],
            'reading_title': image_text_reading['title'],
            'reading_content': image_text_reading['content'],
        }
        image_text_reading_list.append(show_dict)
    image_text_reading_dict = {'image_text_readings': image_text_reading_list}

    # get exhibit video reading info
    video_reading_list = []
    video_readings = OeExhibitionVideoReading.objects.filter(exhibition__id=offset)
    for video_reading in video_readings:
        video_reading = model_to_dict(video_reading)
        show_dict = {
            'id': video_reading['id'],
            'reading_title': video_reading['title'],
            'reading_content': video_reading['content'],
            'video_src': video_reading['video_path'],
            'play_icon': video_reading['play_icon']
        }
        video_reading_list.append(show_dict)
    video_reading_dict = {'audio_readings': video_reading_list}

    reading_dict = {}
    reading_dict = dict(reading_dict, **image_text_reading_dict)
    reading_dict = dict(reading_dict, **video_reading_dict)

    return HttpResponse(json.dumps(reading_dict), content_type='application/json')

def exhibit_image_text_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibit_reading = OeExhibitImageTextReading.objects.filter(id=offset).first()
    exhibit_reading = model_to_dict(exhibit_reading)

    image_text_readings = {
        'id': exhibit_reading['id'],
        'image_path': exhibit_reading['image_path'],
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'
    }

    return HttpResponse(json.dumps(image_text_readings), content_type='application/json')


def exhibit_vedio_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibit_reading = OeExhibitVideoReading.objects.filter(id=offset).first()
    exhibit_reading = model_to_dict(exhibit_reading)

    video_readings = {
        'id': exhibit_reading['id'],
        'video_src': exhibit_reading['video_path'],
        'poster':'/static/exhibition/head1.jpeg',
        'reading_content':'张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
      一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
      他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
      重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
      名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
      黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'
    }
    return HttpResponse(json.dumps(video_readings), content_type='application/json')


def exhibition_image_text_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibition_reading = OeExhibitionImageTextReading.objects.filter(id=offset).first()
    exhibition_reading = model_to_dict(exhibition_reading)

    image_text_readings = {
        'id': exhibition_reading['id'],
        'image_path': exhibition_reading['image_path'],
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'
    }

    return HttpResponse(json.dumps(image_text_readings), content_type='application/json')


def exhibition_vedio_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exhibition_reading = OeExhibitionVideoReading.objects.filter(id=offset).first()
    exhibition_reading = model_to_dict(exhibition_reading)

    video_readings = {
        'id': exhibition_reading['id'],
        'video_src': exhibition_reading['video_path'],
        'poster': '/static/exhibition/head1.jpeg',
        'reading_content': '张大千（Chang Dai-Chien），男,四川内江人，祖籍广东省番禺，1899年5月10日出生于四川省内江市中区城郊安良里的\
          一个书香门第的家庭，中国泼墨画家，书法家。20 世纪50年代，张大千游历世界，获得巨大的国际声誉，被西方艺坛赞为“东方之笔”。[1]\
          他与二哥张善子昆仲创立“大风堂派”，是二十世纪中国画坛最具传奇色彩的泼墨画工。特别在山水画方面卓有成就。后旅居海外，画风工写结合，\
          重彩、水墨融为一体，尤其是泼墨与泼彩，开创了新的艺术风格，因其诗、书、画与齐白石、溥心畲齐名，故又并称为“南张北齐”和“南张北溥”，\
          名号多如牛毛。与黄君璧、溥心畲以“渡海三家”齐名。二十多岁便蓄著一把大胡子，成为张大千日后的特有标志。他曾与齐白石、徐悲鸿、黄君璧、\
          黄宾虹、溥儒、郎静山等及西班牙抽象派画家毕加索交游切磋。'
    }
    return HttpResponse(json.dumps(video_readings), content_type='application/json')

# @csrf_exempt
# def attention(request):
#     if request.method == 'POST':
#         print request.GET.get('artist', '')
#         artist = request.GET.get('artist', '0')
#         attention_count = OeArtist.objects.filter(name=artist).first().attention_count
#
#         Artist.objects.filter(name=artist).update(attention_count=attention_count + 1)
#         return HttpResponse(json.dumps({}), content_type='application/json')
#     if request.method == 'DELETE':
#         print request.GET.get('artist', '')
#         artist = request.GET.get('artist', '0')
#         attention_count = Artist.objects.filter(name=artist).first().attention_count
#
#         Artist.objects.filter(name=artist).update(attention_count=attention_count - 1)
#         return HttpResponse(json.dumps({}), content_type='application/json')
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


def artist_html(request):
    return render_to_response('artist.html', locals())

def production_html(request):
    return render_to_response('production.html', locals())

def exhibition_html(request):
    return render_to_response('exhibition.html', locals())

def home_html(request):
    return render_to_response('home.html', locals())


def motified_signature(request):
    if request.method == 'GET':
        appid = request.GET.get('appid', '0')
        appsecret = request.GET.get('appsecret', 'error')
        from_p = request.GET.get('from', '0')
        isappinstalled = request.GET.get('isappinstalled', 'error')
        url = request.GET.get('url', '0')
        if from_p != 'error' and isappinstalled != 'error':
            url = url + '&from=' + from_p + '&isappinstalled=' + isappinstalled

        wx = Wx(appid, appsecret, url)
        return_dict = {
            'appid': appid,
            'appsecret': appsecret,
            'url': url,
            'access_token': wx.get_access_token,
            'jsapi_ticket': wx.get_jsapi_ticket,
            'timestamp': wx.timestamp,
            'noncestr': wx.noncestr,
            'signature': wx.get_signature()
        }
        OeWxConfig.objects.filter(url=url).update(**return_dict)
        return HttpResponse(json.dumps({}), content_type='application/json')


def get_signature(request):
    if request.method == 'GET':
        appid = request.GET.get('appid', '0')
        appsecret = request.GET.get('appsecret', 'error')
        from_p = request.GET.get('from', '0')
        isappinstalled = request.GET.get('isappinstalled', 'error')
        url = request.GET.get('url', '0')
        if from_p != 'error' and isappinstalled != 'error':
            url = url + '&from=' + from_p + '&isappinstalled=' + isappinstalled
        config = OeWxConfig.objects.filter(url=url, appid=appid, appsecret=appsecret).first()
        if config:
            return_dict = {
                'timestamp': config.timestamp,
                'noncestr': config.noncestr,
                'signature': config.signature
            }
            return HttpResponse(json.dumps(return_dict), content_type='application/json')
        else:
            wx = Wx(appid, appsecret, url)
            return_dict = {
                'appid': appid,
                'appsecret': appsecret,
                'url': url,
                'access_token': wx.get_access_token,
                'jsapi_ticket': wx.get_jsapi_ticket,
                'timestamp': wx.timestamp,
                'noncestr': wx.noncestr,
                'signature': wx.get_signature()
            }
            OeWxConfig.objects.create(**return_dict)

            config = OeWxConfig.objects.filter(url=url, appid=appid, appsecret=appsecret).first()
            return_dict = {
                'timestamp': config.timestamp,
                'noncestr': config.noncestr,
                'signature': config.signature
            }
            return HttpResponse(json.dumps(return_dict), content_type='application/json')
