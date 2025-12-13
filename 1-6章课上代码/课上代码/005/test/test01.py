# -*- coding: utf-8 -*-
# @Time : 2025/12/13 15:16
# @Author : nanji
# @Site : https://geek-docs.com/beautifulsoup/beautifulsoup-questions/186_beautifulsoup_using_soupstrainer_to_parse_selectively.html
# @File : test01.py
# @Software: PyCharm
# @Comment :
from bs4 import BeautifulSoup, SoupStrainer

only_titles = SoupStrainer("h1")
html = "<html><body><h1>标题1</h1><p>段落1</p><h2>标题2</h2><p>段落2</p></body></html>"

soup = BeautifulSoup(html, "html.parser", parse_only=only_titles)

for title in soup:
    print(title.text)
