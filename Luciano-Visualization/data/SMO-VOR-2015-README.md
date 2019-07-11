# SMO VOR dataset

SMO-VOR-2015 is a dataset extracted from John Wiseman's Burbank ADS-B transponder dataset. It lists flights for 2015 that passed within 2km from the [Santa Monica Airport VOR](https://airnav.com/airport/KSMO). Each flight correspond to the closest record for the flight to the VOR.

## Columns

```text
flight: flight name
icao: International Air Transport Association airport code
alt: altitude (feets)
lat: latitude
lon: longitude
dist: distance to the SMO VOR (m)
ptime: penetration time
month: month nome
hour: hour
weekday: day of the week name
ops: Day (6am-midnight) or Night (midnight-5am)
```

## References

- [ICAO Wikipedia page](https://en.wikipedia.org/wiki/ICAO_airport_code)

## Author

Luciano Nocera