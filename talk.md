# Publish Subscribe with RethinkDB

Hi, I'm Josh. I work at RethinkDB as the ecosystem engineer. I'd like
to talk today about a small library I wrote that uses RethinkDB to do
publish subscribe.

How many people are familiar with the publish-subscribe pattern?

Ok, so the gist is that you have some applications that want to talk
to each other, but it's nice if they're not tightly coupled. So, an
example might be following a twitter hashtag. People in Japan can
tweet something with that hashtag and then close the twitter app and
go to sleep. Then you get that tweet in your feed the next time you
open twitter. The idea is that you tell Twitter which kind of messages
you're interested in, and Twitter holds onto them and sends them to
you when you're ready.

-- 1 minute

So the library I wrote is called repubsub. It's actually implemented
in all 3 of our primary languages: JavaScript, Python and Ruby. Here
I'll just be working with the Python version. Let me show you a quick
demo of what it does, then I'll show you how it works:

<open terminal in directory>

```bash
$ ./regex_publish.py
```

This just starts publishing random fake news events about superheroes,
supervillains and sidekicks. Now, somewhere else, we can subscribe to
these messages:

<open another terminal window>

OK, so I want to listen to all news about Robin, so let's do that:

```bash
$ ./regex_subscribe.py '.*Robin'
```

<Show messages scrolling past>

OK, so Robin <some comment about event that shows up>

I can also subscribe to all fights with Batman, Robin or the Joker:

```bash
$ ./regex_subscribe.py 'fights.*(Batman|Hulk)'
```

<Wait for some messages to show up, then Ctrl+C it>

-- 2 minutes

You get the idea. We can use whatever regex we want, let's check out
the code:

<open up the regex_publish code>

So first, we create an exchange. Underneath the covers this becomes a
rethinkDB table.

Then we create a random topic and payload, and publish the payload on
that topic in a loop with a slight delay. Simple.

Next let's look at the subscription code:

<open up regex_subscribe.py>

Just like the publish code, we create an exchange, which connects to a
rethinkDB database.

Here's where pub sub with RethinkDB gets interesting. We can use ReQL
to filter the messages we get, and the server will buffer only the
messages we're interested in in a queue.  Then we just iterate over
messages in the queue and print them out. This uses changefeeds
underneath, so the messages are pushed to us in realtime.

So that's what you can do when the topic is a string. But, since
RethinkDB handles json, we can use whatever we want for a topic. For
example, we could make the topic an array of strings, to filter
something like tags:

```bash
$ ./tags_publish.py
```

OK, and let's subscribe to anything about Batman, Robin, or Joker:

<in another window>

```bash
$ ./tags_subscribe.py or \#Joker \#Batman \#Robin'
```

Or we could subscribe to anything tagged both #fights and #Batman

```bash
$ ./tags_subscribe.py and \#Batman \#fights
```
