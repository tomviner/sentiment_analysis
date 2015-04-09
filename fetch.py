import newspaper
from analyser import sort_articles


sources = [
    'http://www.theguardian.com',
    'http://www.dailymail.co.uk',
    'http://metro.co.uk',
    'http://www.si.com',
    'http://www.bbc.co.uk',
    'http://www.msn.com'
]

articles = []

for source in sources:
    site = newspaper.build(source, memoize_articles=False)
    num_article_source = 0

    for article in site.articles:
        article.download()
        article.parse()

        if len(article.text) > 300:
            articles.append(article.text.replace('\n', ' '))
            num_article_source += 1
            if num_article_source == 5:
                break


_arts = sort_articles(articles)

for art in _arts[:5]:
    print(art[:400])

for art in _arts[25:]:
    print(art[:400])
