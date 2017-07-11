#!/bin/sh

sudo killall uwsgi << hm

sleep 3

uwsgi --ini onlineExhibition_uwsgi.ini