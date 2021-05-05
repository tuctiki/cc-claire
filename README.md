# t66y_spider
利用爬虫下载草榴【新時代的我們】和【達蓋爾的旗幟】两个板块帖子内的图片 
# 环境要求
## 解释器版本
Python 3.x
## 模块列表
pip install -r requirements.txt
## 代理配置
根目录下有代理配置文件，可以配置http/https代理，（参数```[-p 0]```可以禁用代理）<br>
默认配置：
```
{
  "http": "socks5://localhost:1080",
  "https": "socks5://localhost:1080"
}
```
### 本地代理
1. 本地开启ss/ssr/v2ray等服务<br>
2. 设置“允许来自局域网的链接”<br>
3. 修改配置文件```proxy```中的代理端口为ss/ssr/v2ray的本地代理端口（一般默认1080）<br>
*请确保PAC文件设置了代理草榴网站的规则*
### 远程代理
填入代理提供商的IP地址以及对应端口号即可（如socks5://xxx.xxx.xxx.xxx:1234/）
# 使用方法
## 命令行:<br>
```python Spider_of_t66y.py [-h] [-c CLASS_ID] [-s START] [-e END] [-m MAX_THREAD]```<br>
```[-h]``` 显示帮助信息<br>
```[-c]``` 下载类别，```1```下载【新時代的我們】板块 , ```2```下载【達蓋爾的旗幟】板块 , ```0```同时下载两个板块<br>
```[-s]``` 下载的起始页（默认1）<br>
```[-e]``` 下载的尾页<br>
```[-m]``` 设置最大下载线程（默认60）<br>
```[-p]``` '0':禁用代理配置  默认'1'：启用代理 <br>
下载完成的图片会保存在./t66y目录
## example:<br>
```python Spider_of_t66y.py -c 1 -s 1 -e 2 -m 300```<br>
```python Spider_of_t66y.py -c 2 -p 0```<br>
```python Spider_of_t66y.py -h```<br>
