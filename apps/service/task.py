# coding=utf-8
# 有关celery的任务处理。耗时或者定时
import time
import celery


@celery.task
def say_something(word):
    print(word)
    time.sleep(5)
    print('world ...')

