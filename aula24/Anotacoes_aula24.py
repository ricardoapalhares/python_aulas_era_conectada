# 14/03/2019 (quinta-feira)
# Web Scraping
# import scrapy
# 
# Installing Scrapy
# https://docs.scrapy.org/en/latest/intro/install.html
# 
# Tutorial Scrapy
# https://docs.scrapy.org/en/latest/intro/tutorial.html
# 
# mkvirtualenv web-scraping -p python
# Intall miniconda
# conda install -c conda-forge scrapy
# 
# 
# 
# scrapy startproject tutorial
# Create quotes_spider.py dentro da pasta spiders
# 
# 
# scrapy shell "http://quotes.toscrape.com/page/1/"
# 
# response.css('title')
# response.css('title::text').getall()
# response.css('title::text').re(r'Quotes.*')
# response.css('title::text').re(r'(\w+) to (\w+)')
# 
# scrapy shell "http://quotes.toscrape.com"
# 
# tags = quote.css("div.tags a.tag::text").getall()
# tags
# 
# >>> dicionario = {}
# >>> for quote in response.css("div.quote"):
# ...     text = quote.css("span.text::text").get()
# ...     author = quote.css("small.author::text").get()
# ...     tags = quote.css("div.tags a.tag::text").getall()
# ...     dicionario.append(dict(text=text, author=author, tags=tags))
# 
# 
# Fazer projeto com:
#  -> Scrapy (raspar dados)
#  -> Django
#  -> Colocar no github
# 
# 
# 
# 
# 
# 