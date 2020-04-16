import requests
r =requests.get('https://www.amazon.cn/dp/B00A72VZFU/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E4%B9%A6&qid=1587022732&sr=8-1')
r.status_code   
r.encoding
r.encoding = r.apparent_encoding
r.text       
#可以看到结果中有
#<抱歉，我们只是想确认一下当前访问者并非自动程序。为了达到最佳效果，请确保您浏览器上的 Cookie 已启用。
#字样 所以怀疑网站禁止了爬虫的请求 所以改一下头

r.request.headers        #看一下请求头
# User-Agent': 'python-requests/2.22.0'

#现在把头改了
kv = {'user-agent':'Mozilla/5.0'}
#然后重新请求
url = 'https://www.amazon.cn/dp/B00A72VZFU/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E4%B9%A6&qid=1587022732&sr=8-1'
r = requests.get(url,headers = {'user-agent' : 'Mozilla/5.0'})
r.status_code
r.request.headers
r.text

#全代码
import requests
url = 'https://www.amazon.cn/dp/B00A72VZFU/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E4%B9%A6&qid=1587022732&sr=8-1'
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
