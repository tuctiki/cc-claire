# t66y_spider

利用爬虫下载草榴【新時代的我們】和【達蓋爾的旗幟】两个板块帖子内的图片 

# 环境要求

## 解释器版本

Python 3.x

## 模块列表

`pip install -r requirements.txt`

## 代理配置

根目录下有代理配置文件，可以配置http/https代理，不需要代理的可以通过参数`-p 0`禁用

默认配置：
```
{
  "http": "socks5://localhost:1080",
  "https": "socks5://localhost:1080"
}
```

### 本地代理

1. 本地开启`ss/ssr/v2ray`等服务并使用`http`或`socks5`协议监听本地端口

2. 修改配置文件`proxy`中的代理端口为代理程序所监听的端口号
   
*请确保PAC文件设置了代理草榴网站的规则*

### 远程代理

填入代理URL即可，如：`socks5://xxx.xxx.xxx.xxx:1234/`

# 使用方法

## 命令行:

```python Spider_of_t66y.py [-h] [-c CLASS_ID] [-s START] [-e END] [-m MAX_THREAD]```
```[-h]``` 显示帮助信息
```[-c]``` 下载类别，```1```下载【新時代的我們】板块 , ```2```下载【達蓋爾的旗幟】板块 , ```0```同时下载两个板块
```[-s]``` 下载的起始页（默认1）
```[-e]``` 下载的尾页
```[-m]``` 设置最大下载线程（默认64）
```[-p]``` '0':禁用代理配置  默认'1'：启用代理 
下载完成的图片会保存在`./t66y`目录

## example:

```python Spider_of_t66y.py -c 1 -s 1 -e 2 -m 300```
```python Spider_of_t66y.py -c 2 -p 0```
```python Spider_of_t66y.py -h```

# 注意事项

1. 该项目为作者初学Python编程的练习脚本，大部分时间不会维护，**切勿用于非法用途**！

2. 由于众所周知的原因，该网站主域名时常失效，如遇该情况请自行更换`main_url`