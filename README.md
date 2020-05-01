[![gpsTracker Homepage](https://img.shields.io/badge/gpsTracker-develop-orange.svg)](https://github.com/davidvelascogarcia/gpsTracker/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/gpsTracker.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/gpsTracker/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/gpsTracker.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/gpsTracker)

# GPS Tracker: gpsTracker (Python API)

- [Introduction](#introduction)
- [Use](#use)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`gpsTracker` module use `folium` in `python`. This module receive object coordinates with `YARP` port, decode latitude and longitude. `gpsTracker` download location map gets user coordinates and print in the map, saved as `.html`.


## Use

`gpsTracker` requires coordinates like input in `*latitude*+longitude` format.
The process to running the program:

1. Execute [programs/gpsTracker.py](./programs), to start de program.
```python
python gpsTracker.py
```
2. Connect coordinates source.
```bash
yarp connect /yourport/data:o /gpsTracker/data:i
```

NOTE:

- Data results are published on `/gpsTracker/data:o`

## Requirements

`gpsTracker` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install folium:

(Using YARP with Python 2.7 bindings)
```bash
pip2 install folium
```

(Using YARP with Python 3 bindings)
```bash
pip3 install folium
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/gpsTracker.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/gpsTracker)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/gpsTracker.svg?label=Issues)](https://github.com/davidvelascogarcia/gpsTracker/issues)

## Related projects

* [Folium: docs](https://python-visualization.github.io/folium/)

