# Regional sources

The Regional folder provides state-level coverage for all 16 German federal states and local
reporting for a mix of large and medium-sized cities. Keep these feeds in the existing Regional
folder so korall's local-news preset can find them. A catalogue entry is an option for profiles;
it does not select a source or infer a person's location.

## Selection

- State feeds use the [official tagesschau.de regional RSS endpoints](https://www.tagesschau.de/infoservices/rssfeeds).
- City feeds come directly from established local or regional newspaper publishers.
- Add only public, parseable RSS or Atom feeds with entries and recent publication dates.
  An HTTP 200 response alone is insufficient: an empty or abandoned feed adds no coverage.
- Keep publisher and geography visible in titles and descriptions. Broad state coverage is
  useful background; it does not guarantee daily news for a particular town.
- Avoid contributor locations, private profiles and subscription choices in catalogue changes,
  commit messages and public source requests.

## Publisher overlap and article access

The state feeds aggregate reports from the ARD regional broadcasters. For example, WDR and
Tagesschau Nordrhein-Westfalen can carry the same reporting. They are complementary ways to
select coverage, not two independent newsrooms. City editions from the same newspaper also
share reporting; the number of feed URLs is not the number of independent editorial voices.

A useful starting selection is a state broadcaster plus local newspaper reporting. For deeper
local coverage, seek a second local newsroom when it offers a current public feed. Source
variety and the stories actually reaching a section matter more than catalogue size.

Most newspaper feeds offer headlines and short summaries. A working public feed does not imply
that the original article is freely accessible. Miniflux's article fetching can improve available
text but does not guarantee access to subscription articles.

## Feed review on 2026-10-06

All seven existing Regional feeds returned HTTP 200, parsed as RSS or Atom, and contained
recent entries. The expansion adds 30 feeds: 16 state feeds and 14 city feeds, bringing Regional
to 37 sources. Each added feed returned HTTP 200, parsed as RSS, was non-empty and contained
at least one dated entry from the preceding seven days. Latest entries were dated October 5 or 6.

Counts below describe the returned feed window, not total publications over seven days. Feed
sizes and availability can change. These checks do not measure an installation's selected
sources, curation results or successful full-article retrieval. No private profile or installation
data was used.

### Federal states

| State | Feed | Entries in feed |
| --- | --- | ---: |
| Baden-Württemberg | [Tagesschau](https://www.tagesschau.de/inland/regional/badenwuerttemberg/index~rss2.xml) | 59 |
| Bayern | [Tagesschau](https://www.tagesschau.de/inland/regional/bayern/index~rss2.xml) | 58 |
| Berlin | [Tagesschau](https://www.tagesschau.de/inland/regional/berlin/index~rss2.xml) | 59 |
| Brandenburg | [Tagesschau](https://www.tagesschau.de/inland/regional/brandenburg/index~rss2.xml) | 59 |
| Bremen | [Tagesschau](https://www.tagesschau.de/inland/regional/bremen/index~rss2.xml) | 24 |
| Hamburg | [Tagesschau](https://www.tagesschau.de/inland/regional/hamburg/index~rss2.xml) | 13 |
| Hessen | [Tagesschau](https://www.tagesschau.de/inland/regional/hessen/index~rss2.xml) | 59 |
| Mecklenburg-Vorpommern | [Tagesschau](https://www.tagesschau.de/inland/regional/mecklenburgvorpommern/index~rss2.xml) | 23 |
| Niedersachsen | [Tagesschau](https://www.tagesschau.de/inland/regional/niedersachsen/index~rss2.xml) | 29 |
| Nordrhein-Westfalen | [Tagesschau](https://www.tagesschau.de/inland/regional/nordrheinwestfalen/index~rss2.xml) | 59 |
| Rheinland-Pfalz | [Tagesschau](https://www.tagesschau.de/inland/regional/rheinlandpfalz/index~rss2.xml) | 48 |
| Saarland | [Tagesschau](https://www.tagesschau.de/inland/regional/saarland/index~rss2.xml) | 59 |
| Sachsen | [Tagesschau](https://www.tagesschau.de/inland/regional/sachsen/index~rss2.xml) | 24 |
| Sachsen-Anhalt | [Tagesschau](https://www.tagesschau.de/inland/regional/sachsenanhalt/index~rss2.xml) | 32 |
| Schleswig-Holstein | [Tagesschau](https://www.tagesschau.de/inland/regional/schleswigholstein/index~rss2.xml) | 24 |
| Thüringen | [Tagesschau](https://www.tagesschau.de/inland/regional/thueringen/index~rss2.xml) | 54 |

### Cities

Berlin, Hamburg and Bremen are also covered by their separate state feeds and the existing
regional broadcasters. Additional local newspaper feeds:

| City | Publisher feed | Entries in feed |
| --- | --- | ---: |
| Berlin | [Tagesspiegel](https://www.tagesspiegel.de/contentexport/feed/berlin) | 100 |
| Bremen | [Weser-Kurier](https://www.weser-kurier.de/bremen/?view=rss) | 15 |
| Dortmund | [Ruhr Nachrichten](https://www.ruhrnachrichten.de/dortmund/feed/) | 12 |
| Dresden | [Dresdner Neueste Nachrichten](https://www.dnn.de/arc/outboundfeeds/rss/category/lokales/dresden/?outputType=xml) | 17 |
| Duisburg | [Rheinische Post](https://rp-online.de/nrw/staedte/duisburg/feed.rss) | 20 |
| Düsseldorf | [Rheinische Post](https://rp-online.de/nrw/staedte/duesseldorf/feed.rss) | 20 |
| Frankfurt | [Frankfurter Rundschau](https://www.fr.de/frankfurt/rssfeed.rdf) | 40 |
| Hamburg | [Hamburger Abendblatt](https://www.abendblatt.de/hamburg/rss) | 100 |
| Hannover | [Hannoversche Allgemeine](https://www.haz.de/arc/outboundfeeds/rss/category/lokales/hannover/?outputType=xml) | 31 |
| Kassel | [HNA](https://www.hna.de/kassel/rssfeed.rdf) | 40 |
| Köln | [Rheinische Post](https://rp-online.de/nrw/staedte/koeln/feed.rss) | 20 |
| Leipzig | [Leipziger Volkszeitung](https://www.lvz.de/arc/outboundfeeds/rss/category/lokales/leipzig/?outputType=xml) | 56 |
| Moers | [Rheinische Post](https://rp-online.de/nrw/staedte/moers/feed.rss) | 20 |
| München | [Süddeutsche Zeitung](https://rss.sueddeutsche.de/rss/Muenchen) | 15 |
| Nürnberg | [nordbayern](https://www.nordbayern.de/nuernberg?isRss=true) | 27 |
| Offenbach | [Offenbach-Post](https://www.op-online.de/offenbach/rssfeed.rdf) | 40 |
| Potsdam | [Märkische Allgemeine](https://www.maz-online.de/arc/outboundfeeds/rss/category/lokales/potsdam/?outputType=xml) | 20 |
| Trier | [Trierischer Volksfreund](https://www.volksfreund.de/region/trier-trierer-land/feed.rss) | 20 |

### Added 2026-10-29

BR24's Bayern feed (`https://nachrichtenfeeds.br.de/rss/nachrichten/seiten/QXAPkQJ`, 53 entries, all
from br.de/nachrichten/bayern) closes the missing broadcaster for Bayern. City feeds were checked for
their share of local links: Hamburger Abendblatt 99 of 100, Weser-Kurier 14 of 15, Tagesspiegel
Berlin 74 of 100, nordbayern Nürnberg 18 of 27. Saarländischer Rundfunk publishes no public news feed
that could be found (sr.de links none; `index~rss.xml` paths return 404); Saarland keeps the Tagesschau
state feed.

### Excluded candidates

- `https://rp-online.de/nrw/staedte/bonn/feed.rss`: valid RSS with zero entries.
- `https://www.waz.de/staedte/essen/rss`: valid RSS, but its latest entry was dated 2024-06-11.
- `https://www.ksta.de/koeln/feed.rss`: HTTP 410.
- `https://www.stuttgarter-zeitung.de/stuttgart.rss.feed`: HTTP 404. The publisher's general
  feed worked, but included national stories and was not accepted as a city-specific feed.

## After a catalogue update

An administrator confirms the catalogue update in korall. New sources start unselected in every
existing profile. Select the feeds relevant to the profile under Sources and save; adding entries
to this repository does not change a private profile.

korall's section check counts distinct sources behind stored stories over the last seven days,
after at least three editions. Use that result to assess actual coverage once sources are selected.
Feed checks establish a usable catalogue baseline, not a guarantee that every section has enough
relevant stories or independent reporting.

## Validation

For this expansion, `python scripts/check.py --base <previous-catalog.yml>` passed the format,
URL, duplicate, date, version and new-feed reachability checks. Regenerate the matching export
with `python scripts/check.py --opml catalog.opml`. The additional XML, entry and freshness
checks above were performed against the public publisher endpoints during the dated review.
