#!/usr/bin/env python2

import sys

from helpers import regex_colorize, green
import repubsub

if __name__ == '__main__':
    topic_regex = sys.argv[1]
    exchange = repubsub.Exchange('comicbook_events', port=28015, host='localhost')
    reql_filter = lambda topic: topic.match(topic_regex)
    queue = exchange.queue(reql_filter)

    for topic, payload in queue.subscription():
        print '[', regex_colorize(topic, topic_regex), ']'
        print '\t:', green(payload)

