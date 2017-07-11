# -*- coding:utf8 -*-
import json
from django.shortcuts import render_to_response, HttpResponse, Http404
from art.models import OeArtist, OeExhibit, OeExhibition, OeArtistExhibitionRelation
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def artist(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    # artist = OeArtist.objects.filter(id=offset).first()
    # artist_dict = model_to_dict(artist)
    # artist_dict['modify_time'] = artist_dict['modify_time'].strftime('%Y-%m-%d')
    # artist_dict['create_time'] = artist_dict['create_time'].strftime('%Y-%m-%d')

    artist_dict = {
        'avatar': '/static/header/作者.jpeg',
        'name': '大佬',
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
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # production = OeExhibit.objects.filter(id=offset).first()
    # production_dict = model_to_dict(production)

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
    return HttpResponse(json.dumps(exhibits_list[offset]), content_type='application/json')

def exhibits(request):
    exhibit_list=[]
    exhibition = request.GET.get('exhibition', 'error')
    artist = request.GET.get('artist', 'error')
    try:
        exhibition = int(exhibition)
        # exhibits = OeExhibit.objects.filter(exhibition=exhibition)
        # for production in exhibits:
        #     exhibit_list.append(model_to_dict(production))
        # print exhibit_list
        exhibit_list = [
        {
          'id':0,
          'image_path':'/static/exhibit/朝奉图.jpeg',
          'name':'朝奉图',
          'author':'陈某',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            }
          ],
          'ratings':[
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
          'id':1,
          'image_path':'/static/exhibit/树.jpeg',
          'name':'树',
          'author':'康某',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
          'id':2,
          'image_path':'/static/exhibit/景.jpeg',
          'name':'景',
          'author':'大佬',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
          'id':3,
          'image_path':'/static/exhibit/竹子.jpeg',
          'name':'竹子',
          'author':'小佬',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
        return HttpResponse(json.dumps(exhibit_list), content_type='application/json')
    except ValueError:
        print exhibition

    # exhibits = OeExhibit.objects.filter(author=artist)
    # for exhibit in exhibits:
    #     exhibit_list.append(model_to_dict(exhibit))
    # print exhibit_list
    exhibit_list =[
        {
          'id':0,
          'image_path':'/static/exhibit/朝奉图.jpeg',
          'name':'朝奉图',
          'author':'陈某',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
          'id':1,
          'image_path':'/static/exhibit/树.jpeg',
          'name':'树',
          'author':'康某',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
          'id':2,
          'image_path':'/static/exhibit/景.jpeg',
          'name':'景',
          'author':'大佬',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
          'id':3,
          'image_path':'/static/exhibit/竹子.jpeg',
          'name':'竹子',
          'author':'小佬',
          'audio_name':'作品解读',
          'audio_src':'/static/exhibit/lyg.mp3',
          'image_text_readings':[
            {
              'id':0,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            },
            {
              'id':1,
              'image_path':'/static/exhibit/bamboo.jpeg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
            }
          ],
          'audio_readings':[
            {
              'id':0,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'我是来看展览的',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
            },
            {
              'id':1,
              'play_icon':'/static/exhibit/play.svg',
              'reading_title':'好看么',
              'reading_content':'如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
              'video_src':'/static/exhibit/test.mp4',
              'audio_src':'/static/exhibit/lyg.mp3'
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
    return HttpResponse(json.dumps(exhibit_list), content_type='application/json')

def exhibit_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # production = OeExhibit.objects.filter(id=offset).first()
    # production_dict = model_to_dict(production)

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
                },
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
    return HttpResponse(json.dumps(exhibits_list[offset]), content_type='application/json')


@csrf_exempt
def exhibition(request, offset):
    if request.method == 'GET':

        print 'offset=', offset
        try:
            offset = int(offset)
        except ValueError:
            raise Http404()
        # exhibition = OeExhibition.objects.filter(id=offset).first()
        # print exhibition
        # exhibition_dict = model_to_dict(exhibition)
        # exhibition_dict['modify_time'] = exhibition_dict['modify_time'].strftime('%Y-%m-%d')
        # exhibition_dict['create_time'] = exhibition_dict['create_time'].strftime('%Y-%m-%d')

        exhibition_list = [
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
        return HttpResponse(json.dumps(exhibition_list[offset]), content_type='application/json')
    if request.method == 'POST':
        print request.POST.get('a', '0')
        print request.POST.get('b', '0')
        return HttpResponse(json.dumps({}), content_type='application/json')
    if request.method == 'DELETE':
        return HttpResponse(json.dumps({}), content_type='application/json')
    if request.method == 'PUT':
        return HttpResponse(json.dumps({}), content_type='application/json')
    if request.method == 'PATCH':
        return HttpResponse(json.dumps({}), content_type='application/json')


def exhibitions(request):
    exhibition_list = []
    exhibition_id_list = []
    artist = request.GET.get('artist', '0')
    try:
        artist = int(artist)
    except ValueError:
        raise Http404()

    # exhibition_set = OeArtistExhibitionRelation.objects.filter(artist=artist)
    # print exhibition_set
    # for exhibition in exhibition_set:
    #     exhibition_id_list.append(exhibition.exhibiton_id)
    # exhibitions = OeExhibition.objects.filter(id__in=exhibition_id_list)
    # for exhibition in exhibitions:
    #     exhibition_dict = model_to_dict(exhibition)
    #     exhibition_dict['modify_time'] = exhibition_dict['modify_time'].strftime('%Y-%m-%d')
    #     exhibition_dict['created_time'] = exhibition_dict['created_time'].strftime('%Y-%m-%d')
    #     exhibition_list.append(exhibition_dict)
    # print exhibition_list

    exhibition_list = [
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

    return HttpResponse(json.dumps(exhibition_list), content_type='application/json')


def exhibition_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # production = OeExhibit.objects.filter(id=offset).first()
    # production_dict = model_to_dict(production)

    exhibition_list = [
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
                },
                {
                    'image_path': '/static/exhibition/head1.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'image_path': '/static/exhibition/head1.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'image_path': '/static/exhibition/head1.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'image_path': '/static/exhibition/head1.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
                {
                    'image_path': '/static/exhibition/head1.jpeg',
                    'reading_title': '我是来看展览的',
                    'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
                },
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
    ];
    return HttpResponse(json.dumps(exhibition_list[offset]), content_type='application/json')

def image_text_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # production = OeExhibit.objects.filter(id=offset).first()
    # production_dict = model_to_dict(production)

    image_text_readings_list = [
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
        },
        {
            'image_path': '/static/exhibition/head1.jpeg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
        },
        {
            'image_path': '/static/exhibition/head1.jpeg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
        },
        {
            'image_path': '/static/exhibition/head1.jpeg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
        },
        {
            'image_path': '/static/exhibition/head1.jpeg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
        },
        {
            'image_path': '/static/exhibition/head1.jpeg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它'
        }
    ]

    return HttpResponse(json.dumps(image_text_readings_list[offset]), content_type='application/json')


def vedio_readings(request, offset):
    print 'offset=', offset
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # production = OeExhibit.objects.filter(id=offset).first()
    # production_dict = model_to_dict(production)

    vedio_list = [
        {
            'id': 0,
            'play_icon': '/static/exhibition/play.svg',
            'reading_title': '我是来看展览的',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
            'video_src': '/static/exhibition/test.mp4',
            'audio_src': '/static/exhibition/lyg.mp3',
            'poster':'/static/exhibition/head1.jpeg'
        },
        {
            'id': 1,
            'play_icon': '/static/exhibition/play.svg',
            'reading_title': '好看么',
            'reading_content': '如果你无法简介的表达你的想法，那说明你还不够了解它,如果你无法简介的表达你的想法，那说明你还不够了解它',
            'video_src': '/static/exhibition/test.mp4',
            'audio_src': '/static/exhibition/lyg.mp3',
            'poster': '/static/exhibition/head1.jpeg'
        }
    ]
    return HttpResponse(json.dumps(vedio_list[offset]), content_type='application/json')


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
    # introduction = OeArtist.objects.filter(id=artist).first()
    # introduction_dict = model_to_dict(introduction)
    # print introduction_dict['introduction']
    introduction_dict = {
        'introduction': [
            '大佬',
            '1963年出生,江苏苏州人,毕业于苏州工艺美校,苏州大学艺术学院',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员',
            '现为中国美术学家协会会员'
        ]
    }
    return HttpResponse(json.dumps(introduction_dict['introduction']), content_type='application/json')

def achievement(request):
    artist = request.GET.get('artist', '0')
    try:
        artist = int(artist)
    except ValueError:
        raise Http404()
    # achievement = OeArtist.objects.filter(id=artist).first()
    # achievement_dict = model_to_dict(achievement)

    achievement_dict = {
        'achievement':[
            '《水墨变相》(人民美术出版社 2013)',
            '《绘画迹象论》(人民美术出版社 2003)'
        ]
    }
    return HttpResponse(json.dumps(achievement_dict["achievement"]), content_type='application/json')


def artist_html(request):
    return render_to_response('artist.html', locals())

def production_html(request):
    return render_to_response('production.html', locals())

def exhibition_html(request):
    return render_to_response('exhibition.html', locals())

def home_html(request):
    return render_to_response('home.html', locals())

