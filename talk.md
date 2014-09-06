# Publish Subscribe with RethinkDB

Hi, I'm Josh. I work at RethinkDB as the ecosystem engineer. I'd like to
introduce a small library I wrote that uses RethinkDB to do publish subscribe.

How many people are familiar with the publish-subscribe pattern?

Ok, the idea is to decouple communication. An example might be following a
twitter hashtag. Lots of people can post with a hashtag, and other people can
follow the hashtag, and everybody doesn't have to be online at the same time.



-- 1 minute

The library I wrote is called repubsub. It's actually implemented in all 3 of
our primary languages: JavaScript, Python and Ruby, so you can pick whichever
one is best for you. Here I'll just be working with the Python version. Let me
show you a quick demo of what it does, then I'll show you how it works:

<open terminal in directory>

```bash
$ ./pub
```

This just starts publishing random fake news events about superheroes,
supervillains and sidekicks.

Now, somewhere else, we can subscribe to these messages:

<open another terminal window>

OK, so I want to listen to all news involving Batman, Robin or Joker:

```bash
$ ./sub '#fights and #Batman or #Robin or #Joker'
```

You get the idea. Let's check out the code:

<open up the regex_publish code>

So first, we create an exchange. Underneath the covers this becomes a
rethinkDB table.

Then we create a random topic and payload, and publish the payload on
that topic in a loop with a slight delay. Simple.

Next let's look at the subscription code:

<open up regex_subscribe.py>

Just like the publish code, we create an exchange, which connects to a
rethinkDB database.

# Note: rewrite this portion

Here's where pub sub with RethinkDB gets interesting. We can use ReQL
to filter the messages we get, and the server will buffer only the
messages we're interested in in a queue. 

So we get the tags we want to subscribe to from the commandline

Then we create the queue with the filter method and subscribe, just
like before. I added some highlighting since it's hard to see when it
scrolls by quickly.

So, the final bit is: how does this work? Well the idea is that we
just set up a changefeed on a table, and just keep writing to 

# TODO: Show the documents in the data explorer

# Add diagram of queues, exchanges and topics

# Tell them to look up details in the article rethinkdb.com/docs/publish-subscribe
