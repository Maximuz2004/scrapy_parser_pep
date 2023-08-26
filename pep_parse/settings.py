from pathlib import Path


BOT_NAME = "pep_parse"

SPIDER_MODULES = [f"{BOT_NAME}.spiders"]
NEWSPIDER_MODULE = SPIDER_MODULES[0]

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
