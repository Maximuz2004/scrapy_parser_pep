# Асинхронный парсер PEP с использованием Scrapy


Этот проект представляет собой скрипт на языке Python, использующий асинхронный
фреймворк Scrapy для парсинга Python Enhancement Proposals (PEP) с веб-сайта 
Python и извлечения информации о них.

**Стек технологий:**
- [![Python 3.9+](https://img.shields.io/badge/-Python%203.9+-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://docs.python.org/3/),
- [![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://docs.scrapy.org/en/latest/index.html),


## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone git@github.com:Maximuz2004/scrapy_parser_pep.git
   ```

2. Перейдите в папку проекта:

   ```sh
    cd scrapy_parser_pep
   ```
3. Активируйте виртуальное окружение и установите необходимые зависимости:

   ```sh
    pip install -r requirements.txt
   ```

## Использование
Запустите скрипт ```scrapy crawl pep```, в результате работы будет получена 
информация с [сайта](https://peps.python.org/), в директории проекта будет создана 
папка ```results``` с двумя файлами: с информацией о статусах PEP и с небольшой 
сводкой по статусам PEP.



Автор: [Титов Максим](https://github.com/Maximuz2004)
