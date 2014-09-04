#!/usr/bin/env python2

import sys

import repubsub
from helpers import highlight_matching_tags, green

if __name__ == '__main__':

    operator = sys.argv[1]
    subscribed_tags = sys.argv[2:]

    exchange = repubsub.Exchange('comicbook_tags', port=31156, host='newton')

    if operator == 'and':
        reql_filter = lambda topic: topic.contains(*subscribed_tags)
    else:
        reql_filter = lambda topic: topic.set_intersection(subscribed_tags) != []

    queue = exchange.queue(reql_filter)

    for topic_tags, payload in queue.subscription():
        print highlight_matching_tags(subscribed_tags, topic_tags)
        print '\t:', green(payload)
