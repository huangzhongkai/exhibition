from __future__ import unicode_literals

from django.db import models

class OeArtist(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=32) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100) # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX') # Field name made lowercase.
    intro = models.TextField(db_column='INTRO', blank=True) # Field name made lowercase.
    achievement = models.TextField(db_column='ACHIEVEMENT', blank=True) # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BIRTHDATE', blank=True, null=True) # Field name made lowercase.
    head_path = models.CharField(db_column='HEAD_PATH', max_length=200, blank=True) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_artist'

class OeArtistExhibitionRelation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    artist = models.ForeignKey(OeArtist, db_column='ARTIST_ID') # Field name made lowercase.
    exhibiton = models.ForeignKey('OeExhibition', db_column='EXHIBITON_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_artist_exhibition_relation'


class OeExhibit(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=32) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True) # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=100, blank=True) # Field name made lowercase.
    intro = models.TextField(db_column='INTRO', blank=True) # Field name made lowercase.
    image_path = models.CharField(db_column='IMAGE_PATH', max_length=200) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True) # Field name made lowercase.
    category = models.ForeignKey('OeExhibitCategory', db_column='CATEGORY_ID') # Field name made lowercase.
    exhibition = models.ForeignKey('OeExhibition', db_column='EXHIBITION_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibit'

class OeExhibitImageTextReading(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)
    image_path = models.CharField(db_column='IMAGE_PATH', max_length=200)
    title = models.CharField(db_column='TITLE', max_length=100, blank=True)
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True)
    exhibit = models.ForeignKey('OeExhibit', db_column='EXHIBIT_ID')
    class Meta:
        db_table = 'oe_exhibit_image_text_reading'

class OeExhibitVideoReading(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)
    video_path = models.CharField(db_column='VIDEO_PATH', max_length=200)
    title = models.CharField(db_column='TITLE', max_length=100, blank=True)
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True)
    play_icon = models.CharField(db_column='PLAY_ICON', max_length=200)
    exhibit = models.ForeignKey('OeExhibit', db_column='EXHIBIT_ID')
    class Meta:
        db_table = 'oe_exhibit_video_reading'


class OeExhibitCategory(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200) # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=1000, blank=True) # Field name made lowercase.
    parent = models.ForeignKey('self', db_column='PARENT_ID', blank=True, null=True) # Field name made lowercase.
    deleted = models.CharField(db_column='DELETED', max_length=1) # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibit_category'

class OeExhibitComment(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    content = models.TextField(db_column='CONTENT') # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    exhibit = models.ForeignKey(OeExhibit, db_column='EXHIBIT_ID', blank=True, null=True) # Field name made lowercase.
    parent = models.ForeignKey('self', db_column='PARENT_ID', blank=True, null=True) # Field name made lowercase.
    user = models.ForeignKey('OeUser', db_column='USER_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibit_comment'

class OeExhibition(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50) # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME') # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True) # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=32) # Field name made lowercase.
    intro = models.TextField(db_column='INTRO') # Field name made lowercase.
    image_path = models.CharField(db_column='IMAGE_PATH', max_length=200) # Field name made lowercase.
    audio_path = models.CharField(db_column='AUDIO_PATH', max_length=200, blank=True) # Field name made lowercase.
    video_path = models.CharField(db_column='VIDEO_PATH', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibition'

class OeExhibitionImageTextReading(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)
    image_path = models.CharField(db_column='IMAGE_PATH', max_length=200)
    title = models.CharField(db_column='TITLE', max_length=100, blank=True)
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True)
    exhibition = models.ForeignKey('OeExhibition', db_column='EXHIBITION_ID')
    class Meta:
        db_table = 'oe_exhibition_image_text_reading'

class OeExhibitionVideoReading(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)
    video_path = models.CharField(db_column='VIDEO_PATH', max_length=200)
    title = models.CharField(db_column='TITLE', max_length=100, blank=True)
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True)
    play_icon = models.CharField(db_column='PLAY_ICON', max_length=200)
    exhibition = models.ForeignKey('OeExhibition', db_column='EXHIBITION_ID')
    class Meta:
        db_table = 'oe_exhibition_video_reading'

class OeExhibitionComment(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    content = models.TextField(db_column='CONTENT') # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    exhibition = models.ForeignKey(OeExhibition, db_column='EXHIBITION_ID', blank=True, null=True) # Field name made lowercase.
    parent = models.ForeignKey('self', db_column='PARENT_ID', blank=True, null=True) # Field name made lowercase.
    user = models.ForeignKey('OeUser', db_column='USER_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibition_comment'

class OeExhibitionImage(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    pic_type = models.CharField(db_column='PIC_TYPE', max_length=32) # Field name made lowercase.
    exhibition = models.ForeignKey(OeExhibition, db_column='EXHIBITION_ID') # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=500) # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True) # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True) # Field name made lowercase.
    size = models.BigIntegerField(db_column='SIZE', blank=True, null=True) # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UPLOAD_TIME') # Field name made lowercase.
    enabled = models.CharField(db_column='ENABLED', max_length=1) # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibition_image'

class OeExhibitionInterpretation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200) # Field name made lowercase.
    exhibition = models.ForeignKey(OeExhibition, db_column='EXHIBITION_ID') # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=2) # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=32) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    modify_by = models.CharField(db_column='MODIFY_BY', max_length=32, blank=True) # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True) # Field name made lowercase.
    origin = models.CharField(db_column='ORIGIN', max_length=200, blank=True) # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=45, blank=True) # Field name made lowercase.
    publish_time = models.DateTimeField(db_column='PUBLISH_TIME', blank=True, null=True) # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True) # Field name made lowercase.
    file_path = models.CharField(db_column='FILE_PATH', max_length=128, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibition_interpretation'

class OeExhibitionRecommend(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    exhibition = models.ForeignKey(OeExhibition, db_column='EXHIBITION_ID') # Field name made lowercase.
    recommend_type = models.CharField(db_column='RECOMMEND_TYPE', max_length=4) # Field name made lowercase.
    recommend_no = models.IntegerField(db_column='RECOMMEND_NO') # Field name made lowercase.
    class Meta:
        db_table = 'oe_exhibition_recommend'

class OeImageType(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20) # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True) # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True) # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True) # Field name made lowercase.
    max_size = models.BigIntegerField(db_column='MAX_SIZE', blank=True, null=True) # Field name made lowercase.
    pattern = models.CharField(db_column='PATTERN', max_length=100, blank=True) # Field name made lowercase.
    upload_path = models.CharField(db_column='UPLOAD_PATH', max_length=100, blank=True) # Field name made lowercase.
    defaul_img_path = models.CharField(db_column='DEFAUL_IMG_PATH', max_length=200, blank=True) # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=8, blank=True) # Field name made lowercase.
    max_copies = models.IntegerField(db_column='MAX_COPIES', blank=True, null=True) # Field name made lowercase.
    enabled = models.CharField(db_column='ENABLED', max_length=1, blank=True) # Field name made lowercase.
    deleted = models.CharField(db_column='DELETED', max_length=1, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_image_type'

class OeNotify(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True) # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=2) # Field name made lowercase.
    target = models.CharField(db_column='TARGET', max_length=32, blank=True) # Field name made lowercase.
    target_type = models.CharField(db_column='TARGET_TYPE', max_length=45, blank=True) # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=45, blank=True) # Field name made lowercase.
    sender = models.CharField(db_column='SENDER', max_length=32, blank=True) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    class Meta:
        db_table = 'oe_notify'

class OeSubscription(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    target = models.CharField(db_column='TARGET', max_length=32) # Field name made lowercase.
    target_type = models.CharField(db_column='TARGET_TYPE', max_length=45) # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=45, blank=True) # Field name made lowercase.
    user = models.ForeignKey('OeUser', db_column='USER_ID') # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    class Meta:
        db_table = 'oe_subscription'

class OeSysLog(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    log_type = models.CharField(db_column='LOG_TYPE', max_length=4) # Field name made lowercase.
    log_level = models.CharField(db_column='LOG_LEVEL', max_length=8, blank=True) # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=128) # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=16) # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE') # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_log'

class OeSysMenu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    menu_name = models.CharField(db_column='MENU_NAME', max_length=50) # Field name made lowercase.
    menu_path = models.CharField(db_column='MENU_PATH', max_length=255, blank=True) # Field name made lowercase.
    is_leaf_menu = models.IntegerField(db_column='IS_LEAF_MENU') # Field name made lowercase.
    menu_order = models.IntegerField(db_column='MENU_ORDER') # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE') # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=50, blank=True) # Field name made lowercase.
    parent = models.ForeignKey('self', db_column='PARENT_ID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_menu'

class OeSysParamInfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    para_name = models.CharField(db_column='PARA_NAME', max_length=32) # Field name made lowercase.
    para_type = models.ForeignKey('OeSysParamType', db_column='PARA_TYPE') # Field name made lowercase.
    para_val = models.CharField(db_column='PARA_VAL', max_length=64) # Field name made lowercase.
    para_desc = models.CharField(db_column='PARA_DESC', max_length=256, blank=True) # Field name made lowercase.
    enabled = models.IntegerField(db_column='ENABLED') # Field name made lowercase.
    is_sys_def_para = models.CharField(db_column='IS_SYS_DEF_PARA', max_length=1) # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=16) # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE') # Field name made lowercase.
    modify_by = models.CharField(db_column='MODIFY_BY', max_length=16, blank=True) # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE', blank=True, null=True) # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED') # Field name made lowercase.
    para_code = models.CharField(db_column='PARA_CODE', max_length=32) # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_param_info'

class OeSysParamType(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME', max_length=32) # Field name made lowercase.
    type_desc = models.CharField(db_column='TYPE_DESC', max_length=64, blank=True) # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=16, blank=True) # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE') # Field name made lowercase.
    modify_by = models.CharField(db_column='MODIFY_BY', max_length=16, blank=True) # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE', blank=True, null=True) # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED') # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=8) # Field name made lowercase.
    enabled = models.IntegerField(db_column='ENABLED') # Field name made lowercase.
    is_sys_def_para = models.CharField(db_column='IS_SYS_DEF_PARA', max_length=1) # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_param_type'

class OeSysStyleIcons(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    icon_name = models.CharField(db_column='ICON_NAME', max_length=256, blank=True) # Field name made lowercase.
    icon_style = models.CharField(db_column='ICON_STYLE', max_length=256, blank=True) # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True) # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE') # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=16, blank=True) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True) # Field name made lowercase.
    modify_by = models.CharField(db_column='MODIFY_BY', max_length=16, blank=True) # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True) # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_style_icons'

class OeSysUser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100) # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=64) # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE') # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=200, blank=True) # Field name made lowercase.
    cellphone = models.CharField(db_column='CELLPHONE', max_length=11, blank=True) # Field name made lowercase.
    realname = models.CharField(db_column='REALNAME', max_length=32, blank=True) # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE', blank=True, null=True) # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_sys_user'

class OeUser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=200, blank=True) # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=200, blank=True) # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=200) # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', default=0) # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True) # Field name made lowercase.
    head_path = models.CharField(db_column='HEAD_PATH', max_length=200, blank=True) # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BIRTHDATE', blank=True, null=True) # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True) # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=11, blank=True) # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=100, blank=True) # Field name made lowercase.
    wechat = models.CharField(db_column='WECHAT', max_length=100, blank=True) # Field name made lowercase.
    micro_blog = models.CharField(db_column='MICRO_BLOG', max_length=100, blank=True) # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'oe_user'

class OeUserExhibitCollection(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    user = models.ForeignKey(OeUser, db_column='USER_ID') # Field name made lowercase.
    exhibit = models.ForeignKey(OeExhibit, db_column='EXHIBIT_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_user_exhibit_collection'

class OeUserExhibitionCollection(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    user = models.ForeignKey(OeUser, db_column='USER_ID') # Field name made lowercase.
    exhibition = models.ForeignKey(OeExhibition, db_column='EXHIBITION_ID') # Field name made lowercase.
    class Meta:
        db_table = 'oe_user_exhibition_collection'

class OeUserNotify(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    is_read = models.CharField(db_column='IS_READ', max_length=1) # Field name made lowercase.
    user = models.ForeignKey(OeUser, db_column='USER_ID') # Field name made lowercase.
    notify = models.ForeignKey(OeNotify, db_column='NOTIFY_ID') # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME') # Field name made lowercase.
    class Meta:
        db_table = 'oe_user_notify'

class OeUserRelation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32) # Field name made lowercase.
    user = models.ForeignKey(OeUser, db_column='USER_ID', related_name='re_status') # Field name made lowercase.
    follow_user = models.ForeignKey(OeUser, db_column='FOLLOW_USER_ID', related_name='follow_user') # Field name made lowercase.
    re_status = models.CharField(db_column='RE_STATUS', max_length=1) # Field name made lowercase.
    class Meta:
        db_table = 'oe_user_relation'

class OeWxConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    appid = models.CharField(db_column='APPID', max_length=100)
    appsecret = models.CharField(db_column='APPSECRET', max_length=100)
    access_token = models.CharField(db_column='ACCESS_TOKEN', max_length=200)
    jsapi_ticket = models.CharField(db_column='JSAPI_TICKET', max_length=200)
    signature = models.CharField(db_column='SIGNATURE', max_length=100)
    timestamp = models.IntegerField(db_column='TIMESTAMP', default=0)
    noncestr = models.CharField(db_column='NONCESTR', max_length=30)
    url = models.CharField(db_column='URL', max_length=100)
    class Meta:
        db_table = 'oe_wx_config'

