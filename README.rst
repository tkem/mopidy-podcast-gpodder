Mopidy-Podcast-gpodder.net
========================================================================

Mopidy-Podcast-gpodder.net is a Mopidy-Podcast_ v1.x extension for
searching and browsing podcasts using the `gpodder.net`_ Web service.

Status
------------------------------------------------------------------------

`gpodder.net`_ support has been an experiment and a proof of concept
to test out the Mopidy-Podcast v1.0 API for alternate podcast
directory support more than anything else.

At this point in time, it is not being actively worked on, and is no
longer compatible with Mopidy-Podcast v2.0.  If you are interested in
fixing this please do get in touch or start sending pull requests :-)


Installation
------------------------------------------------------------------------

First, make sure you have Mopidy-Podcast version 1.x installed.  Note
that this extension is *not* compatible with Mopidy-Podcast 2.0 and
later.  Then Mopidy-Podcast-gpodder.net can be installed by running::

    pip install Mopidy-Podcast-gpodder.net


Configuration
------------------------------------------------------------------------

The default configuration contains everything to get you up and
running, and will usually require only a few modifications to match
personal preferences::

    [podcast-gpodder]
    enabled = true

    # gpodder.net base URL
    base_url = http://gpodder.net/

    # user-friendly name for browsing the gpodder.net root directory
    root_name = gpodder.net

    # format string for tag (top-level) results; field names are: tag,
    # usage
    tag_format = {tag}

    # format string for podcast results; field names are: description,
    # subscribers, subscribers_last_week, title, url, website
    podcast_format = {title}

    # default number of tags or podcasts to show when browsing
    count = 20

    # HTTP request timeout in seconds
    timeout = 10


Project Resources
------------------------------------------------------------------------

.. image:: http://img.shields.io/pypi/v/Mopidy-Podcast-gpodder.net.svg
    :target: https://pypi.python.org/pypi/Mopidy-Podcast-gpodder.net/
    :alt: Latest PyPI version

.. image:: http://img.shields.io/pypi/dm/Mopidy-Podcast-gpodder.net.svg
    :target: https://pypi.python.org/pypi/Mopidy-Podcast-gpodder.net/
    :alt: Number of PyPI downloads

- `Issue Tracker`_
- `Source Code`_
- `Change Log`_
- `Development Snapshot`_


License
------------------------------------------------------------------------

Copyright (c) 2014 Thomas Kemmer.

Licensed under the `Apache License, Version 2.0`_.


.. _Mopidy-Podcast: https://github.com/tkem/mopidy-podcast
.. _gpodder.net: http://gpodder.net
.. _APT repository: http://apt.kemmer.co.at/
.. _Issue Tracker: https://github.com/tkem/mopidy-podcast-gpodder/issues/
.. _Source Code: https://github.com/tkem/mopidy-podcast-gpodder
.. _Change Log: https://raw.github.com/tkem/mopidy-podcast-gpodder/master/Changes
.. _Development Snapshot: https://github.com/tkem/mopidy-podcast-gpodder/tarball/master#egg=Mopidy-Podcast-gpodder.net-dev

.. _Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
