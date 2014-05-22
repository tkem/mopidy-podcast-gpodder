Mopidy-Podcast-gpodder.net
========================================================================

Mopidy-Podcast-gpodder.net is a Mopidy-Podcast_ extension for
searching and browsing podcasts on `gpodder.net`_.


Installation
------------------------------------------------------------------------

First, make sure you have Mopidy-Podcast version 1.0.0 or later
installed.  Then Mopidy-Podcast-gpodder.net can be installed by
running::

    pip install Mopidy-Podcast-gpodder.net

After a restart, Mopidy-Podcast will pick up the installed extension
automatically.

You can also download and install Debian/Ubuntu packages for
Mopidy-Podcast-gpodder.net releases_.


Configuration
------------------------------------------------------------------------

The default configuration contains everything to get you up and
running, and will usually require only a few modifications to match
personal needs::

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

.. _releases: https://github.com/tkem/mopidy-podcast-gpodder/releases
.. _Issue Tracker: https://github.com/tkem/mopidy-podcast-gpodder/issues/
.. _Source Code: https://github.com/tkem/mopidy-podcast-gpodder
.. _Change Log: https://raw.github.com/tkem/mopidy-podcast-gpodder/master/Changes
.. _Development Snapshot: https://github.com/tkem/mopidy-podcast-gpodder/tarball/master#egg=Mopidy-Podcast-gpodder.net-dev

.. _Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
