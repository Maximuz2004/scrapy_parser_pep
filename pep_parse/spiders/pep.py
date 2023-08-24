import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        for pep in response.css('#numerical-index tbody tr'):
            yield response.follow(
                pep.css('a.pep.reference.internal::attr(href)').get(),
                callback=self.parse_pep,
                cb_kwargs={
                    'pep_number': pep.css(
                        'a.pep.reference.internal::text'
                    ).get()
                }
            )

    def parse_pep(self, response, pep_number):
        yield PepParseItem(
            {
                'number': pep_number,
                'name': response.css(
                    '.page-title::text'
                ).get().split(' – ')[1],
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get(),
            }
        )
