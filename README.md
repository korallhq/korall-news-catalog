# korall news catalog

The source catalogue of [korall](https://korall.news), a hosted personal news service: a reviewed list
of RSS and Atom feeds, grouped in folders, with a short description for each source.

- [`catalog.yml`](catalog.yml) is the catalogue korall reads.
- [`catalog.opml`](catalog.opml) is generated from it for any other RSS app.

## How korall uses it

The korall platform fetches `catalog.yml` from `main` once an hour and keeps the last valid document.
Only a strictly newer `version` replaces it, so every change raises the version; rolling back means
publishing a new, higher version with the old content.

- Every profile sees every catalogue source. Profiles in automatic mode (the default for new
  profiles) adopt matching new sources by themselves; manual profiles get them as recommendations.
- Moved feeds listed under `replaces` keep their place in profiles.
- Sources listed under `removed` leave the catalogue; customers' own sources are never affected.

Changes arrive by pull request; the CI checks the format and that the version moves forward.
New sources also appear in the korall.news Logbuch.

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
    topics: [Nachrichten, Politik]           # optional, several focus labels
    regions: [Deutschland]                  # optional, explicit reporting areas
    publisher_type: public                  # public, editorial, specialist, official, other
    kinds: [national, public]               # optional, overlapping facets
    added: 2026-10-06            # on new sources
    replaces: https://old.example/feed.xml   # when a feed moved
removed:                         # dead or discontinued feeds
- url: https://dead.example/rss
  title: Example
  removed: 2026-10-06
  reason: Feed eingestellt.
```

## Regional coverage

`topics`, `regions` and `kinds` are optional discovery metadata, not assignments to a profile's
sections. `publisher_type` describes the publisher independently of topic and reporting area. All 216 sources
have a type: public broadcaster, newsroom, specialist site, first-party organisation/company or unclassified.
`regions` lists German federal states only, also for a city feed; korall knows no finer reporting
area and uses it as a search filter. When a reader names a place for a section, korall derives its
federal state and recommends that state's broadcasters plus local feeds whose title or description
names the town (local feeds start their description with "Lokalnachrichten … aus <Ort>"); otherwise
readers choose regional sources with that filter. A source is shown once even when
several filters match it. Leave unknown reporting areas empty. Existing source IDs and
subscriptions stay intact.

The **Regional** folder includes a separate ARD feed for every German federal state, existing
regional broadcasters, and local reporting from a mix of large and medium-sized cities.
See the [regional source review](docs/regional-sources.md) for coverage, publisher overlap and
the dated feed checks. Public RSS access does not imply access to the full article.

Catalogue availability alone does not populate a section: administrators confirm catalogue
updates, and each profile selects the sources relevant to its region. State feeds can complement
local reporting, but are not a substitute for city feeds or a second independent newsroom.

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
