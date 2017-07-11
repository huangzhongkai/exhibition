from django.test import TestCase

# Create your tests here.

# class Artist(models.Model):
#     name = models.CharField(max_length=100L, default='')
#     production_count = models.IntegerField(default=0)
#     attention_count = models.IntegerField(default=0)
#     introduction = models.CharField(max_length=1000L, default='')
#     achievement = models.CharField(max_length=1000L, default='')
#     avatar = models.CharField(max_length=200L, default='')
#     background = models.CharField(max_length=200L, blank=True, default='')
#
#     class Meta:
#         db_table = 'artist'
#
#     def __unicode__(self):
#         return self.name
#
#
# class Exhibition(models.Model):
#     artist_name = models.ForeignKey(Artist, default='')
#     exhibition_name = models.CharField(max_length=30L, default='')
#     exhibition_image = models.CharField(max_length=200L, default='')
#     exhibition_date = models.CharField(max_length=200L, default='')
#     exhibition_site = models.CharField(max_length=200L, default='')
#     curator = models.CharField(max_length=30L, default='')
#     audio_src = models.CharField(max_length=1000L, default='')
#     audio_name = models.CharField(max_length=30L, default='未知音乐')
#     class Meta:
#         db_table = 'exhibition'
#
#     def __unicode__(self):
#             return self.exhibition_name
#
# class Production(models.Model):
#     artist_name = models.ForeignKey(Artist, null=True)
#     production_image = models.CharField(max_length=200L, default='')
#     production_name = models.CharField(max_length=30L, default='')
#     production_author = models.CharField(max_length=30L, default='')
#     audio_src = models.CharField(max_length=1000L, default='')
#     audio_name = models.CharField(max_length=30L, default='未知音乐')
#     class Meta:
#         db_table = 'production'
#
#     def __unicode__(self):
#             return self.production_name