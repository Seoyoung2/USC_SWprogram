# README

The dataset contains average traffic speed on freeway segments in LA for 7-9am and 4-7pm on both directions for M-F week days:

- 2016: week of May 30 - June 3 and week of June 13-17
- 2017: week of May 29 - June 2 and week of June 12-16
- 2018: week of May 28 - June 1 and week of June 11-15

The dataset contains average speed data for links (sensors) on segments corresponding to the following freeways:

- I-405: Interstate 405, also known as the San Diego Freeway is a major __north–south__ Interstate Highway in Southern California.
- I-10: Interstate 10 is the southernmost cross-country (__east-west__) interstate highway in the American Interstate Highway System.
- I-5: Interstate 5 is a major __north–south__ route of the Interstate Highway System in the U.S. state of California.
- SR-101: U.S. Route 101, or U.S. Highway 101 is a __north–south__ United States Numbered Highway
- I-110: Route 110, consisting of State Route 110 and Interstate 110, is a state highway in the Los Angeles metropolitan area of the U.S. state of California, built to freeway standards. The entire route connects San Pedro and the Port of Los Angeles with Downtown Los Angeles and Pasadena (__north–south__).
- SR-105: Interstate 105 is an Interstate Highway in southern Los Angeles County, California that runs __east–west__ from near the Los Angeles International Airport to the City of Norwalk.
- SR-710: Interstate 710, is a state highway in the Los Angeles area of the U.S. state of California, built to Interstate Highway standards. State Route 710 is the completed portion of the proposed northern extension of the route to Pasadena (__north–south__).
- SR-605: Interstate 605 is a major __north–south__ Interstate Highway in the Greater Los Angeles urban area of Southern California, running about 27 miles in length from Seal Beach to Duarte.
- I-210: Route 210, consisting of the contiguous segments of Interstate 210 and State Route 210 forming the Foothill Freeway, is a major __east–west__ state highway in the Greater Los Angeles urban area of the U.S. state of California.

## Data files

- Freeway segments details are in `segments.csv`
- Link sensor detail in `links.csv`
- Average speed for segments and links is provided CSV files named after the corresponding segment.

## Data dictionary

`<segment-name>.csv`:

- segment: freeway segment label (from `segments.csv`)
- date: date in YYYYMMDD format
- direction: either N, S, E, or W depending on freeway
- time: either 7-9AM or 4-7PM
- link: sensor id (sensor detail from `links.csv`)
- speed: average speed of link in miles/hour

Freeway segments are described in `segments.csv`

- segments: name of freeway section
- intersection: other freeways delimiting the segment
- latA, lonA,latB,lonB: lat, lon coordinates of segment
