# korall news catalog

The source catalogue of [korall](https://korall.news), a self-hosted news curator: a reviewed list
of RSS and Atom feeds, grouped in folders, with a short description for each source.

- [`catalog.yml`](catalog.yml) is the catalogue korall reads.
- [`catalog.opml`](catalog.opml) is generated from it for any other RSS app.

## How korall uses it

Every korall image ships a copy of this catalogue. Administrators may choose
**Settings → Source catalogue → Official korall catalogue** to receive changes between releases.
korall then loads `catalog.yml` from this repository (HTTPS, at most every six hours) and offers
what changed since its last update under **Sources**. Nothing changes without the administrator's
confirmation:

- new sources join the library unselected in every profile and are marked “New”;
- moved feeds keep their place in profiles and direct subscriptions;
- removed sources are deleted only when ticked, and never while a profile receives them directly.

## Format

```yaml
version: 2026-10-06              # raise with every change; same day again: 2026-10-06.2
folders:
- title: Nachrichten
  sources:
  - title: Tagesschau
    url: https://www.tagesschau.de/xml/rss2/
    website: https://www.tagesschau.de/
    description: Kurze Beschreibung auf Deutsch.
    added: 2026-10-06            # on new sources
    replaces: https://old.example/feed.xml   # when a feed moved
removed:                         # dead or discontinued feeds
- url: https://dead.example/rss
  title: Example
  removed: 2026-10-06
  reason: Feed eingestellt.
```

## Contributing

**Missing sources for a topic?** Open an issue with the “Sources wanted” form – korall links there
from sections that have hardly any sources.


Pull requests are welcome. A source should be a working public feed, reputable, and useful to
more than one person. Date new entries with `added`, raise `version`, and keep descriptions short
and factual (German for now). The check runs on every pull request: format, public addresses
only, no duplicates, dates not after the version, a raised version, and reachability of new feeds.

```sh
pip install PyYAML
python scripts/check.py
```

## License

The catalogue is dedicated to the public domain under [CC0 1.0](LICENSE). Feeds and their content
belong to their publishers.
