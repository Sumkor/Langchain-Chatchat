import html2text

h = html2text.HTML2Text()
h.ignore_links = False
print(h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!"))

html = '<h1>标题</h1><p>这是一篇带图片的文档。</p><h2>图片一</h2><p>这是一张带着文字的图片</p><p><img src="http://ihome-scm.oss-cn-shenzhen.aliyuncs.com/1724232841.1956148.png" /></p><h2>图片二</h2><p>这是一张绿色帽子狗狗的图片：</p><p><img src="http://ihome-scm.oss-cn-shenzhen.aliyuncs.com/1724232841.3854194.png" /></p><p>图片三</p><p>这是一张白色狗狗的图片</p><p>![白色狗狗的图片](https://tse2-mm.cn.bing.net/th/id/OIP-C.FRZh6FryVcYvQa5KVRpUCwHaFj?rs=1&amp;pid=ImgDetMain)</p><h2>图片四</h2><p>这是一张白色狗狗的图片地址</p><p>https://tse2-mm.cn.bing.net/th/id/OIP-C.FRZh6FryVcYvQa5KVRpUCwHaFj?rs=1&amp;pid=ImgDetMain</p>';

print(h.handle(html))

from markdownify import markdownify

print(markdownify(html))

