import re
import scrapy
from urllib.parse import urlparse
from attack_surface.items import AttackSurfaceItem

class AtkSurfSpider(scrapy.Spider):
    name = "atksurf"

    def start_requests(self):
        with open("targets.txt") as f:
            for url in f:
                yield scrapy.Request(url=url.strip(), callback=self.parse)

    def parse(self, response):
        item = AttackSurfaceItem()

        # Basic
        item["url"] = response.url
        item["domain"] = urlparse(response.url).netloc
        item["title"] = response.css("title::text").get()
        item["status"] = response.status

        # Headers
        x_powered = response.headers.get("X-Powered-By", b"").decode()
        server = response.headers.get("Server", b"").decode()
        content_type = response.headers.get("Content-Type", b"").decode()

        item["server"] = server
        item["content_type"] = content_type

        # Server and X-Powered-By Versions
        versions = []

        server_match = re.search(r"([a-zA-Z\-]+)/([\d\.]+)", server)
        if(server_match):
            versions.append(f"{server_match.group(1)} {server_match.group(2)}")

        x_powered_match = re.search(r"([a-zA-Z\-]+)/([\d\.]+)", x_powered)
        if(x_powered_match):
            versions.append(f"{x_powered_match.group(1)} {x_powered_match.group(2)}")

        generator = response.css('meta[name="generator"]::attr(content)').get()

        if(generator):
            versions.append(generator)

        item["versions"] = list(set(versions))

        # Technologies
        technologies = []
        html = response.text.lower()

        # CMS
        if "wp-content" in html or "wordpress" in html:
            technologies.append("WordPress")

        if "joomla" in html:
            technologies.append("Joomla")

        if "drupal" in html:
            technologies.append("Drupal")

        # Frontend
        if "react" in html:
            technologies.append("React")

        if "angular" in html:
            technologies.append("Angular")

        if "vue" in html:
            technologies.append("Vue")

        # Languages/Frameworks
        x_powered_lower = x_powered.lower()

        if "php" in html or "php" in x_powered_lower:
            technologies.append("PHP")

        if "django" in html:
            technologies.append("Django")

        if "laravel" in html:
            technologies.append("Laravel")

        if "node.js" in html or "express" in html or "express" in x_powered_lower:
            technologies.append("Node.js")

        item["technologies"] = list(set(technologies))

        # Endpoints
        links = response.css("a::attr(href)").getall()

        endpoints = []
        base_domain = urlparse(response.url).netloc

        for link in links:
            full_url = response.urljoin(link)
            if(urlparse(full_url).netloc.endswith(base_domain)):
                endpoints.append(full_url)

                # Follows crawl
                yield scrapy.Request(full_url, callback=self.parse)
        
        item["endpoints"] = list(set(endpoints))

        yield item
