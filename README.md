# Scrapy for Crawling Thairath Online

This is a crawler that I've built for scraping info from https://www.matichon.co.th/politics

### Installing

First, you might want to clone this repository
```
$ git clone https://github.com/naponjatusripitak/matichon_project

```
### Deployment

To run the crawler:
```
$ scrapy crawl matichon_bot

```

To run the crawler with persistence (pause with ctrl-c and resume by rerunning the code):

```
$ scrapy crawl matichon_bot -s JOBDIR=crawl/matichon_bot

```

A csv file named 'matichon.csv' should show up in your directory.

### Changing the settings

There are several ways to fine tune the crawler. For instance, you may want to adjust the number of concurrent request in settings.py

```
#CONCURRENT_REQUESTS = 32

```
Or change the type of output


```
FEED_FORMAT = "csv" # or 'txt'
```

## Happy Scraping!