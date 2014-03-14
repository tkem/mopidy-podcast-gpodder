Mopidy-Podcast-gpodder.net
========================================================================

Mopidy-Podcast-gpodder.net is a Mopidy-Podcast_ extension for
searching and browsing podcasts on `gpodder.net`_.


Installation
------------------------------------------------------------------------

Like other Mopidy extensions, Mopidy-Podcast-gpodder.net can be
installed using pip by running::

    pip install Mopidy-Podcast-gpodder.net

You can also download and install Debian/Ubuntu packages for
Mopidy-Podcast-gpodder.net releases_.


Configuration
------------------------------------------------------------------------

Configuration items are still subject to change at this point, so be
warned::

    [podcast-gpodder]
    enabled = true

    # user-friendly name for browsing, etc.
    display_name = gpodder.net

    # gpodder.net base URL
    base_url = http://gpodder.net/

    # number of tags to show up in browsing
    top_tags_count = 20

    # number of podcasts to show up in browsing
    podcasts_count = 20

    # optional http request timeout in seconds
    timeout =


Project Resources
------------------------------------------------------------------------

- `Source Code`_
- `Issue Tracker`_
- `Change Log`_
- `Development Snapshot`_

.. image:: https://pypip.in/v/Mopidy-Podcast-gpodder.net/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Podcast-gpodder.net/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/Mopidy-Podcast-gpodder.net/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Podcast-gpodder.net/
    :alt: Number of PyPI downloads


License
------------------------------------------------------------------------

Mopidy-Podcast-gpodder.net is Copyright 2014 Thomas Kemmer.

Licensed under the `Apache License, Version 2.0`_.


.. _Mopidy-Podcast: https://github.com/tkem/mopidy-podcast
.. _gpodder.net: http://gpodder.net
.. _releases: https://github.com/tkem/mopidy-podcast-gpodder/releases
.. _Source Code: https://github.com/tkem/mopidy-podcast-gpodder
.. _Issue Tracker: https://github.com/tkem/mopidy-podcast-gpodder/issues/
.. _Change Log: https://github.com/tkem/mopidy-podcast-gpodder/blob/master/Changes
.. _Development Snapshot: https://github.com/tkem/mopidy-podcast-gpodder/tarball/master#egg=Mopidy-Podcast-gpodder.net-dev
.. _Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
