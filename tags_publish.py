#!/usr/bin/env python2
import sys
import time

import repubsub
from helpers import random_tags, green, get_speed


if __name__ == '__main__':
    speed = get_speed(sys.argv)
    exchange = repubsub.Exchange('comicbook_tags', port=31156, host='newton')
    
    while True:
        tags, payload = random_tags()

        print ' '.join(tags)
        print '\t:', green(payload)

        exchange.topic(tags).publish(payload)

        time.sleep(speed)
