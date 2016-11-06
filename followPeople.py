#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot
import getId
import os
import getUsers
import time
import random

bot = InstaBot(login="__________", password="_____________",
               like_per_day=0,
               comments_per_day=0,
               tag_list=[],
               max_like_for_one_tag=50,
               follow_per_day=10000,
               follow_time=12*60*60,
               unfollow_per_day=0,
               unfollow_break_min=10000,
               unfollow_break_max=100000,
               log_mod=0)

os.system("touch users.txt")

users = getUsers.getUsers()

f = open("users.txt", "w")

for user in users.keys():
    bot.like(users[user])
    sec = 2 + random.random()
    time.sleep(sec)
    print("Following: " + user)
    bot.follow(getId(user))
    f.write(user + "\n")
    pause = random.randint(23,25)
    pause += random.random()
    time.sleep(pause)
