import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
                '#numerical-index tbody tr a.pep.reference.internal'
        ):
            yield response.follow(
                pep_link.attrib['href'],
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        pep_title = response.css('.page-title::text').get().split(' – ')
        yield PepParseItem(
            dict(
                number=pep_title[0].split()[1],
                name=pep_title[1],
                status=response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get()
            )
        )
