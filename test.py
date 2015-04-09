
from analyser import sort_articles

articles = (
    "worst bad awful bad bad bad thing. but worse",
    "really good, nice things and a pixie"
)

sorted_articles = sort_articles(articles)

assert sorted_articles == articles
