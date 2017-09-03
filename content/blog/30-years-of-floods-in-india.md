---
title : "30 years of floods in India"
date : "2017-09-03T19:01:00+05:30"
tags : ["data", "visualization", "climate", "blag"]
draft : false
---

{{<figure src="/images/30-years-flooding.png">}}

Inspired by [this post](https://www.axios.com/thirty-years-of-major-flooding-in-the-united-states-2479957846.html) showing the major flooding events in the US, I created a
similar graphic for India. You can find an interactive version [here](https://punchagan.github.io/data-projects/30-years-floods/) -- hovering
over each flooding, shows some more information about the event.

-   The graphic uses flooding related data from the [Dartmouth Flood Observatory](http://www.dartmouth.edu/~floods/Archives/index.html).
-   The data for 2017 events may not be up-to date.
-   The flood severity is indicated by the color of each shape
-   Each shape represents the [geographic flood extents](http://www.dartmouth.edu/~floods/Archives/ArchiveNotes.html) - based on information
    obtained from news sources.
-   The data for India map shape is obtained from this [topojson collection](https://github.com/deldersveld/topojson/tree/master/countries/india)

It is interesting to look at the severity definitions [here](http://floodobservatory.colorado.edu/Archives/ArchiveNotes.html) -- the extreme class
floods, for instance, are defined to be those that have an estimated recurrence
interval of over 100 years. In a span of 30 odd years, there are a whole bunch
of regions which have been affected by extreme floods. Yet another case in point
showing that the climate change shit has really hit the roof!


## Code {#code}

I used `ogr2ogr` to convert the shape file obtained from the Dartmouth Flood
Observatory

```sh
ogr2ogr -f geoJSON data/floods.json FloodArchive_region.shp
```

This file turned out to be about 6MB. I created a file with only Indian floods
by parsing the json file.

```python
import json

with open('floods.json', encoding='latin-1') as f:
    data = json.load(f)

india_features = [
    feature for feature in data['features']
    if feature['properties']['COUNTRY'] == 'India'
]
data['features'] = india_features

with open('india-floods.json', 'w', encoding='latin-1') as f:
    json.dump(data, f)
```

The visualization code itself is about a [hundred odd lines of d3 code](https://github.com/punchagan/data-projects/blob/master/30-years-floods/viz.js).
