# import scrapy

# class ScratchQoutes(scrapy.Spider):
#     name='quotes'
#     start_urls=["https://quotes.toscrape.com/"]
    
#     def parse(self,response):
#         print("\n\n\n\n\n----------------")
#         print(f"The URL is {response.url}")
#         print(f"The header is {response.headers.get('Content-Length')}")
#         print(response.body.decode('utf-8'))
#         print('\n\n\n\n\n\n\n')


import scrapy

# class QuoteScraper(scrapy.Spider):
#     name="quotes"
#     start_urls=['https://quotes.toscrape.com/']
    
#     def parse(self,response):
        
#         for quote in response.css('.text::text').getall():
#             yield{
#                 'Quotes':quote
#             }

class QouteScraper(scrapy.Spider):
    name="quote"
    start_urls=['https://quotes.toscrape.com/']
    
    def parse(self,response):
        
        for div in response.css('.quote'):
            yield{
                'Quote':div.css('.text::text').get(),
                'Author':div.css('.author::text').get()
            }