# Demons specification

A Demons server allows shared channel of communications between group of
people based on an HTTP URL and a channel NAME.

Channels are created implicitely.

Posts are textual, possibly with some configurable size limit.

Posts are numbered and timestamped automatically.

Posts are only available for a configurable time on server setup, by default
1 minute.

Different user agents (client software) allow to access the service and
are interoperable.

An initial implementation is available [here](flask/).

User agents can involve various technologies and be
a CLI
([curses](https://docs.python.org/3/howto/curses.html),
[urwid](http://urwid.org/)),
a GUI
([GTK](https://www.gtk.org/),
[AWT](https://fr.wikipedia.org/wiki/Abstract_Window_Toolkit),
[Swing](https://fr.wikipedia.org/wiki/Swing_%28Java%29),
[JavaFX](https://openjfx.io/),
[Qt](https://www.qt.io/),
[tkinter](https://docs.python.org/3.7/library/tk.html),
[wxWidgets](https://www.wxwidgets.org/)),
a web app
([Bootstrap](https://getbootstrap.com/),
[jQuery](https://jquery.com/),
[VueJS](https://vuejs.org/),
[React](https://reactjs.org/),
[Angular](https://angularjs.org)),
a mobile app
([Kotlin](https://kotlinlang.org/),
[Swift](https://www.apple.com/swift/),
[React-native](https://www.reactnative.com/),
[Ionic](https://ionicframework.com/),
[Flutter](https://flutter.dev/))…

The server can use various framework, such as:
[Flask](https://flask.palletsprojects.com/),
[django](https://www.djangoproject.com/) or
[NodeJS](https://nodejs.org/).

Data are stored in
SQL databases
[sqlite](https://www.sqlite.org/),
[Postgres](https://www.postgresql.org),
[anosql](https://pypi.org/project/anosql/) or
NoSQL variants
[MongoDB](https://www.mongodb.com/)…

Various development, build, deployment environments can be used,
such as [StackBlitz](https://stackblitz.com) or [CodePen](https://codepen.io/).

Here are some user stories to implement at your leisure.

See also [Matrix](https://matrix.org/).

## User Story 0: MVP server (already implemented)

An administrator starts a Demons server and provides the corresponding
URL to people who may use it.

The server provides the following API, which return json data if appropriate

    URL/NAME/get/N # return channel NAME message number N
    URL/NAME/pull # return all available channel NAME messages
    URL/NAME/pull/N # return channel NAME messages with number >= N
    URL/NAME/post/some_message # do a short direct post, return post number

A message is a `json` dictionnary:

```json
{
  "id": 42,
  "ts": "1970-03-20 05:12:31",
  "content": "The Ultimate Question of Life, the Universe and Everything"
}
```

## User Story 1: MVP client (already implemented)

The user connects to the URL and gets a very basic web app, which allows to:

  * show messages on a channel
  * change the current channel
  * post to the current channel

## User Story 2: Better client - POST

A user posts a message with URL on channel NAME, which is stored temporarily
in the server.

## User Story 3: Better client - GET N

A user retrieve one message based on URL, NAME and its number, if available.

## User Story 4: Better client - PULL

A user retrieves all messages posted recently with the URL and NAME.

## User Story 5: Better client - PULL N

A user retrieves available recent messages starting from a given number
with URL and NAME.

## User Story 6: Better client - encrypted channel

A channel may be encrypted, but the server does not need to know.

This should be interoperable between clients.

## User Story 7: Better client - MIME

A user may post picture, audio, video or document messages,
but the server does not need to know it is one.

This should be interoperable between clients.

## User Story 8: Better client - geolocation

A user may emit its position which is displayed on a map.

## User Story 9: Better server - POST

Server and client can post with HTTP parameter `content`.

    URL/NAME/post # append message to channel ("content" HTTP parameter), return post number

Consider extending the server further, for instance:

    URL/NAME/get # return all available messages on channel NAME
    URL/NAME/delete/N # delete message number N
    URL/NAME/clear # clear all messages from channel NAME
    URL/NAME/clear/N # clear all channel NAME messages up to N

## User Story A: Better client - DELETE N

A user may delete a post with URL on channel NAME.

## User Story B: Better client - disconnected

The UI tells when the server is not responding.

## User Story C: Better client - Bootstrap

A bloke told you to do it with [Bootstrap](https://getbootstrap.com/) because it is cool.

## User Story D: Different server - MongoDB

A bloke told you to do it with [MongoDB](https://www.mongodb.com/) because it is cool.

## User Story E: Different server - NodeJS

A bloke told you to do it with [NodeJS](https://nodejs.org/) because it is cool.

## User Story F: Different server - Django

A bloke told you to do it with [django](https://www.djangoproject.com//) because it is cool.

## User Story G: Different server and client - Socket.IO

A bloke told you to do it with [Socket.IO](https://socket.io/) because it is cool.

## User Story H: Different server - CGI & ASP

An old bloke told you they used to do it with [CGI](https://fr.wikipedia.org/wiki/Common_Gateway_Interface/)
or [ASP](https://en.wikipedia.org/wiki/Active_Server_Pages).

## User Story I: Better server - reconfigured delay

A specific channel may dynamically be reconfigured to another expiration delay.

## User Story J: Better server - explicit channels

Channels are explicitely created, with the creator having administrative rights.

## User Story Z: Better client or server

Add your own extension!
