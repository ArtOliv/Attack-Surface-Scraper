# 🕷️ Attack Surface Scraper

**Languages:** [Portuguese](README.md) | [English](README.en.md)

---

Scrapy-based crawler developed as a `passive reconnaissance tool` to collect public website data, focusing on **attack surface mapping**.

---

## Overview

This project crawls a **list of targets** and extracts relevant information for security analysis, such as:

* Basic website information
* Technologies used
* Exposed versions
* HTTP headers
* Internal endpoints

The data is exported in a structured JSON format for further analysis.

---

## Features

* Crawling multiple domains
* Internal endpoint discovery
* Technology fingerprinting (frontend, backend, CMS)
* Version extraction via headers and meta tags
* Automatic JSON export
* Rate limiting and depth control (Scrapy feature)

---

## Project Structure

```
Attack-Surface-Scraper/
│
├── attack_surface/
|   ├── attack_surface/
|   |   ├── spiders/
|   |   │   └── attack_surface_spider.py
|   |   ├── items.py
|   |   ├── middlewares.py
|   |   ├── pipelines.py
|   |   └── settings.py
│   ├── scrapy.cfg
|   └── targets.txt
|
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Attack-Surface-Scraper.git
cd Attack-Surface-Scraper
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to use

### 1. Define targets

Edit the `targets.txt` file:

```
https://example.com
https://test.vulnweb.com
```

### 2. Change to crawler directory

```bash
cd attack_surface
```

### 3. Run the crawler

```bash
scrapy crawl atksurf
```

### 4. Output

The data will be automatically saved to:

```
attack_surface/data/output.json
```

---

## Output Structure (JSON)

Example output:

```json
{
  "url": "https://example.com",
  "domain": "example.com",
  "title": "Example Domain",
  "status": 200,
  "server": "Apache/2.4.52",
  "content_type": "text/html",
  "technologies": ["Apache", "PHP"],
  "versions": ["Apache 2.4.52", "PHP 8.1.2"],
  "endpoints": [
    "https://example.com/about",
    "https://example.com/contact"
  ]
}
```

---

## How It Works

1. Reads targets from `targets.txt`
2. Sends HTTP requests to each domain
3. Extracts:
   * HTML
   * Headers
   * Internal links
4. Applies heuristics to identify technologies
5. Continues crawling while respecting:
   * Domain scope
   * Website policies
   * Depth (`DEPTH_LIMIT`)
6. Exports structured data

---

## Crawler Configuration

In the `settings.py` file:

* `DEPTH_LIMIT` → controls crawl depth
* `DOWNLOAD_DELAY` → helps avoid blocking
* `AUTOTHROTTLE_ENABLED` → automatic rate adjustment
* `ROBOTSTXT_OBEY` → respects site bot policies

---

## Limitations

* Technology detection is heuristic-based due to obfuscation techniques
* Versions may be hidden or masked
* Does not replace vulnerability scanners

---

## Possible Improvements

* Risk classification
* Integration with external APIs
* Database export

---

## Author

`Arthur Carvalho Rodrigues Oliveira`

Project developed for cybersecurity and data mining studies. Data collection is limited to **publicly available information**, so use responsibly and ethically.

---

## License

This project is licensed under the MIT License — feel free to use, modify, and adapt it.
