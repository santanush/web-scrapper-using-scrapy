import scrapy


class PriceBabaMobileListParser(scrapy.Spider):
    name = 'mobileParser'
    allowed_domains = ["pricebaba.com"]
    start_urls = ["https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india"]
    page_value = 2
    no_of_pages=400

    def parse(self, response):
        divdata = response.xpath('//div[@class="prd-crd prd-crd-v p-b-xs p-h-s pos-rel "]')
        print("***********************************************")
        print(divdata)
        for data in divdata:
            mobile = data.xpath('./div[2]/a/text()').extract_first()
            price = data.xpath('./div[2]/div[1]/div[1]/span/text()').extract_first()

            yield {
                'Mobile': mobile,
                'Price' : price
            }
        next_page = response.xpath('//span[text()="Next"]/@data-href').extract_first()
        print('Next page link extracted', next_page)
        if (next_page):
            try:
                next_page = next_page
                print('******************************Next page is :', next_page)
                self.page_value = self.page_value + 1
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
            except Exception as e:
                print(e)
                print("Error............")
        else:
            print('*******************************************************************next page cannot be retrieved')

        print('Completed the scrapping')

