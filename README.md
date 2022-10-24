# PySleepMe (Works but abandoned) 

I got rid of my Dock Pro - so I don't really care aobut this project so much :)


[![pypi](https://img.shields.io/pypi/v/pysleepme.svg)](https://pypi.org/project/pysleepme/)
[![python](https://img.shields.io/pypi/pyversions/pysleepme.svg)](https://pypi.org/project/pysleepme/)
[![Build Status](https://github.com/jeeftor/pysleepme/actions/workflows/dev.yml/badge.svg)](https://github.com/jeeftor/pysleepme/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/jeeftor/pysleepme/branch/main/graphs/badge.svg)](https://codecov.io/github/jeeftor/pysleepme)



Python [Sleep Me API](https://docs.developer.sleep.me/api/) Wrapper for Home Assistant Use


* Documentation: <https://jeeftor.github.io/pysleepme>
* GitHub: <https://github.com/jeeftor/pysleepme>
* PyPI: <https://pypi.org/project/pysleepme/>
* Free software: MIT

# TODO

- [ ] - Have them actually ship my order
- [x] - Code API to query devices
- [ ] - Code API Calls for specific device
- [ ] - Add control logic

## Background

The SleepMe API documentation is available [here](https://docs.developer.sleep.me/api/). This library uses [openapi-python-client](https://www.google.com/search?client=safari&rls=en&q=openapi-python-client&ie=UTF-8&oe=UTF-8) with a slightly modified version of the API (there is an issue with one of the endpoint names) to create an OpenAPI 3.0 client.

This library then wraps those features for easier usage.
## Quickstart

First you must get an API Token this is done somewhere:
