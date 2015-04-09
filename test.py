from analyser import sort_articles


def test_sorting():
    articles = [
        "worst bad awful bad bad bad thing. but worse",
        "dog",
        "cat",
        "neutral",
        "really good, nice things and a pixie",
        "happy awesome amazing fabulous ice cream and chocolate",
    ]

    sorted_articles = sort_articles(articles)

    assert sorted_articles == articles
