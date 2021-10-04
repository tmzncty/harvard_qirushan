# 尝试获得书的预览URL
# 那一堆书店地址是
"""
https://hollis.harvard.edu/primo-explore/search?query=lsr38,exact,Harvard-Yenching%20Library%20Chinese%20
Rare%20Books%20Digitization%20Project-%20Qi%20Rushan%20collection,AND&tab=books&search_scope=default_scope&sortby=rank&v
id=HVD2&mode=advanced&offset=0
"""
# 很长吧，先获取个页面
import requests
Url = "https://hollis.harvard.edu/primo-explore/search?query=lsr38,exact,Harvard-Yenching%20Library%20Chinese%20Rare%20Books%20Digitization%20Project-%20Qi%20Rushan%20collection,AND&tab=books&search_scope=default_scope&sortby=rank&vid=HVD2&facet=rtype,include,books&mode=advanced&offset=0"
print(requests.get(Url))
r = requests.get('https://api.github.com/events')
print(r)