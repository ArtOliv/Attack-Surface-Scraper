import scrapy

class AttackSurfaceItem(scrapy.Item):
    # Basic
    url = scrapy.Field()
    domain = scrapy.Field()
    title = scrapy.Field()
    status = scrapy.Field()

    # Headers
    server = scrapy.Field()
    content_type = scrapy.Field()

    # Versions
    versions = scrapy.Field()

    # Technologies
    technologies = scrapy.Field()

    # Endpoints
    endpoints = scrapy.Field()
