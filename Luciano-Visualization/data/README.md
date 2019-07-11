# SMO VOR dataset

## Description

SMO-VOR-2015 is a dataset extracted from John Wiseman's Burbank ADS-B transponder dataset of 2015 for flights within 2km from the Santa Monica Airport VOR. Each flight correspond to the closest record for the flight to the VOR.

## Files

```bash
SMO-VOR-2015.csv
```

## Columns

```text
flight: flight name
icao: International Air Transport Association airport code
alt: altitude (m)
lat: latitude
lon: longitude
dist: distance to the SMO VOR
ptime: penetration time
month: month nome
hour: hour
weekday: day of the week name
ops: Day (6am-midnight) or Night (midnight-5am)
```

## References

- [Wikipedia page](https://en.wikipedia.org/wiki/ICAO_airport_code)

## Author

[Luciano Nocera](mailto:nocera@usc.edu)