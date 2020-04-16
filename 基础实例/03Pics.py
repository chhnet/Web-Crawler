
#思路
import requests
path = 'D://abc.jpg'
url = 'http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg'
r= requests.get(url)
r.status_code
with open(path,'wb') as f:
    f.write(r.content)
f.close

#整理
import os,requests
url = 'http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg'
root = 'D://pics//'
path = root + url.split('/')[-1]  #取到图片的原始名字
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
