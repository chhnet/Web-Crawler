# Web Spider

## 一、爬虫规则

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416143620375.png" alt="image-20200416143620375" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416143848998.png" alt="image-20200416143848998" style="zoom:50%;" />

- ### 通用框架

`

```python
try:
	r = requests.get(url,timeout = 30)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	return r.text
except:
	return "产生异常"
```



- ### Robots协议

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416151935220.png" alt="image-20200416151935220" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416152001438.png" alt="image-20200416152001438" style="zoom:50%;" />

- ### 爬虫实战

  京东

  亚马逊（更改了请求头）

  图片

  

## 二、信息提取（Beautiful Soup）

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416202946754.png" alt="image-20200416202946754" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200416204135567.png" alt="image-20200416204135567" style="zoom:50%;" />

​                                                                      

#                          信息组织与提取

#### 信息标记的三种形式

1. XML

   <img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175424177.png" alt="image-20200417175424177" style="zoom:30%;" /><img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175622313.png" alt="image-20200417175622313" style="zoom:33%;" />

2. JSON

   <img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175526337.png" alt="image-20200417175526337" style="zoom:33%;" />![image-20200417175648330](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175648330.png)<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175526337.png" alt="image-20200417175526337" style="zoom:33%;" />![image-20200417175648330](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175648330.png)

3. YAML

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175551520.png" alt="image-20200417175551520" style="zoom:33%;" />![image-20200417175705544](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175705544.png)<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175551520.png" alt="image-20200417175551520" style="zoom:33%;" />![image-20200417175705544](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417175705544.png)



## 							实例：大学排名定向爬取

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200417214120735.png" alt="image-20200417214120735" style="zoom:50%;" />

## 三、爬虫实战

### 1.正则表达式

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423165349145.png" alt="image-20200423165349145" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423165423911.png" alt="image-20200423165423911" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423165444549.png" alt="image-20200423165444549" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423165546512.png" alt="image-20200423165546512" style="zoom:50%;" />

### 2.Re库介绍

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423213924084.png" alt="image-20200423213924084" style="zoom:50%;" />![image-20200423213946873](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423213946873.png)

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423213924084.png" alt="image-20200423213924084" style="zoom:50%;" />![image-20200423213946873](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423213946873.png)![image-20200423214123152](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214123152.png)

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214235712.png" alt="image-20200423214235712" style="zoom:50%;" />![image-20200423214254833](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214254833.png)

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214235712.png" alt="image-20200423214235712" style="zoom:50%;" />![image-20200423214254833](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214254833.png)![image-20200423214314761](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214314761.png)

![image-20200423214314761](C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200423214314761.png)

# 四、爬虫框架

## 1、结构

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200427211618051.png" alt="image-20200427211618051" style="zoom:50%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200427211654428.png" alt="image-20200427211654428" style="zoom:50%;" />

## 2.常用命令

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200427211731668.png" alt="image-20200427211731668" style="zoom:67%;" />

## 3.yield关键字

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200427211834800.png" alt="image-20200427211834800" style="zoom:67%;" />

<img src="C:\Users\Hw\AppData\Roaming\Typora\typora-user-images\image-20200427211857233.png" alt="image-20200427211857233" style="zoom:67%;" />