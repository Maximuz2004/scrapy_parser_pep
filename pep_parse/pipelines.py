from collections import defaultdict
from datetime import datetime
import csv

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from .settings import BASE_DIR, RESULT_DIR, TIME_FORMAT

FILE_SAVED_MESSAGE = 'Файл с результатами был сохранен: {}'
NO_STATUS_ERROR_MESSAGE = 'Отсутствует статус PEP'
FIELD_NAMES = ['Статус', 'Количество']
FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def __init__(self):
        self.status_counts = defaultdict(int)
        self.result_dir = BASE_DIR / RESULT_DIR
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = ItemAdapter(item).get('status')
        if status is None:
            raise DropItem(NO_STATUS_ERROR_MESSAGE)
        self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime(TIME_FORMAT)
        file_path = self.result_dir / FILE_NAME.format(now)
        data_to_write = [
            {FIELD_NAMES[0]: status, FIELD_NAMES[1]: count}
            for status, count in self.status_counts.items()
        ]
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=FIELD_NAMES,
                dialect=csv.unix_dialect
            )
            writer.writeheader()
            writer.writerows(data_to_write)
            writer.writerow(
                {
                    FIELD_NAMES[0]: 'Total',
                    FIELD_NAMES[1]: sum(self.status_counts.values())
                }
            )
        spider.log(FILE_SAVED_MESSAGE.format(file_path))
