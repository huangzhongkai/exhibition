#!/bin/sh

killall -9 uwsgi

uwsgi --ini onlineExhibition_uwsgi.ini