import scrapy

class ScratchQoutes(scrapy.Spider):
    name='quotes'
    start_urls=["https://quotes.toscrape.com/"]
    
    def parse(self,response):
        print("\n\n\n\n\n----------------")
        print(f"The URL is {response.url}")
        print(f"The header is {response.headers.get('Content-Length')}")
        print(response.body.decode('utf-8'))
        
        
        print('\n\n\n\n\n\n\n')