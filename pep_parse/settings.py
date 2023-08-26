from pathlib import Path


NEWSPIDER_MODULE = "pep_parse.spiders"
SPIDER_MODULES = [NEWSPIDER_MODULE]

BASE_DIR = Path(__file__).parent.parent
RESULT_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

ROBOTSTXT_OBEY = True

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
