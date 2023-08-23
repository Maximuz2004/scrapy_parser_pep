import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org"]

    def parse(self, response):
        all_peps = response.css('#numerical-index tbody tr')
        for pep in all_peps:
            url = pep.css('a.pep.reference.internal::attr(href)').get()
            pep_number = pep.css('a.pep.reference.internal::text').get()
            yield response.follow(
                url,
                callback=self.parse_pep,
                cb_kwargs={'pep_number': pep_number}
            )



    def parse_pep(self, response, pep_number):

        data = {
            'number': pep_number,
            'name': response.css('.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }

        yield PepParseItem(data)