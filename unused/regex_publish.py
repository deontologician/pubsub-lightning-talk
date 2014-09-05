#!/usr/bin/env python2

import sys
import time

from helpers import random_topic_key, get_speed, green
import repubsub


if __name__ == '__main__':
    speed = get_speed(sys.argv)
    exchange = repubsub.Exchange('comicbook_events', port=28015, host='localhost')

    while True:
        topic_key, payload = random_topic_key()

        print '[', topic_key, ']'
        print '\t:', green(payload)

        exchange.topic(topic_key).publish(payload)

        time.sleep(speed)
