from pathlib import Path


BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

BASE_DIR = Path(__file__).parent.parent
RESULT_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
FEEDS = {
f'{RESULT_DIR}/pep_%(time)s.csv': {
'format': 'csv',
'fields': ['number', 'name', 'status'],
'overwrite': True
},
}

