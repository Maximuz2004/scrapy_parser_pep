from collections import defaultdict
from datetime import datetime
import csv

from .settings import BASE_DIR, RESULT_DIR, TIME_FORMAT

FILE_SAVED_MESSAGE = 'Файл с результатами был сохранен: {}'
NO_STATUS_ERROR_MESSAGE = 'Отсутствует статус PEP'
PEP_TITLE = ('Статус', 'Количество')
TOTAL_NAME = 'Общее количество'
FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def __init__(self):
        self.result_dir = BASE_DIR / RESULT_DIR
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        file_path = self.result_dir / FILE_NAME.format(
            datetime.now().strftime(TIME_FORMAT)
        )
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    PEP_TITLE,
                    *self.status_counts.items(),
                    (TOTAL_NAME, sum(self.status_counts.values()))
                ]
            )

        spider.log(FILE_SAVED_MESSAGE.format(file_path))
