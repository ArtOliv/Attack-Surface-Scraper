# 🕷️ Attack Surface Scraper

Crawler com Scrapy desenvolvido para ser uma `passive reconnaissance tool` para coleta de informações públicas de websites com foco em **mapeamento de superfície de ataque**.

---

## Descrição Geral

Este projeto realiza o crawling de uma **lista de targets** e extrai informações relevantes para análise de segurança, como:

* Informações básicas do site
* Tecnologias utilizadas
* Versões expostas
* Headers HTTP
* Endpoints internos

Os dados são exportados em formato JSON estruturado para análise posterior.

---

## Funcionalidades

* Crawling de múltiplos domínios
* Coleta de endpoints internos
* Fingerprinting de tecnologias (frontend, backend, CMS)
* Extração de versões via headers e meta tags
* Exportação automática em JSON
* Configuração de rate limit e depth control (funcionalidade do Scrapy)

---

## Estrutura do Projeto

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

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Attack-Surface-Scraper.git
cd Attack-Surface-Scraper
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Como usar

### 1. Defina os alvos

Edite o arquivo `targets.txt`:

```
https://example.com
https://test.vulnweb.com
```

---

### 2. Execute o crawler

```bash
scrapy crawl atksurf
```

---

### 3. Output

Os dados serão salvos automaticamente em:

```
attack_surface/data/output.json
```

---

## Estrutura da saída (JSON)

Exemplo de saída:

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

## Como funciona

1. Lê os alvos do arquivo `targets.txt`
2. Faz requisições HTTP para cada domínio
3. Extrai:
   * HTML
   * Headers
   * Links internos
4. Aplica heurísticas para identificar tecnologias
5. Continua o crawling respeitando:
   * Domínio
   * Políticas do site
   * Profundidade (`DEPTH_LIMIT`)
6. Exporta os dados estruturados

---

## Configurações do crowler

No arquivo `settings.py`:

* `DEPTH_LIMIT` -> controla profundidade do crawl
* `DOWNLOAD_DELAY` -> evita bloqueios
* `AUTOTHROTTLE_ENABLED` -> ajuste automático de velocidade
* `ROBOTSTXT_OBEY` -> respeita comportamento de bots nos sites

---

## Limitações

* Detecção de tecnologias é baseada em heurísticas devido a métodos de ocultação
* Versões podem estar ocultas ou mascaradas
* Não substitui ferramentas como scanners de vulnerabilidade

---

## Possíveis melhorias

* Classificação de risco
* Integração com APIs externas
* Exportação para banco de dados

---

## Autor

`Arthur Carvalho Rodrigues Oliveira`

Projeto desenvolvido para estudo em cybersegurança e mineração de dados. A coleta é feita apenas em **dados públicos**, portanto use de forma ética e responsável.

---

## Licença

Este projeto está licenciado sob a MIT License — Sinta-se à vontade para utilizar, modificar e adaptar.
