# 我想到哪写哪，不一定准确
## 1.最初的想法
[书的链接](https://hollis.harvard.edu/primo-explore/search?query=lsr38,exact,Harvard-Yenching%20Library%20Chinese%20Rare%20Books%20Digitization%20Project-%20Qi%20Rushan%20collection,AND&tab=books&search_scope=default_scope&sortby=rank&vid=HVD2&mode=advanced&offset=0)
本来是说先获取所有书的链接，再取每本书具体内容的。分析一下上面的源代码，可以看出不是写在HTML里面的。
这样一来，就分析一下具体的书。比如说 [新刻出像點板時尚崑腔雜出醉怡情 : 8卷 / 菰蘆釣叟點次.\[China\] : 古吳致和堂, 清初, \[i.e. between 1644 and 1735\] 8 册.](https://iiif.lib.harvard.edu/manifests/view/drs:15005787$1i)
分析一下链接，你是不是发现了什么。
首先是头部都随意，但是drs后面就是书的编号，然后1是书的页码，是不是就很明确了。

接下来就很好办了，我就打算写代码了。
## 但是
去看一下json文件，找到default.jpg你会发现编号基本上都是一样的，json文件感谢哈佛大学提供在右上角那个i的图标处，点开即可。
这样就直接IDM批量下载，\*作为通配符写一下就行。
### 然而，你觉得事情有这么简单？
的确没有，挂着代理下载，然后确认页数，一本一本的下载，最后合成PDF。

## 最后
如果要的人直接拿吧。
https://tmzncty.cn/post/174/
