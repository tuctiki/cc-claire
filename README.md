# t66y_spider
下载草榴【新時代的我們】和【達蓋爾的旗幟】两个板块帖子内的图片 
# 环境要求
## python版本
python 3.x
## 所需模块
pip install requirements.txt
## 代理配置
需要开启全局代理(ss/ssr)
# 使用方法
命令行:
```python Spider_of_t66y.py [-h] [-c CLASS_ID] [-s START] [-e END] [-m MAX_THREAD]```
[-h]:x显示帮助信息
[-c]:下载类别，'1'下载【新時代的我們】板块,'2'下载【達蓋爾的旗幟】板块,'0'同时下载两个板块
[-s]:下载的起始页
[-e]:下载的尾页
[-m]:最大下载线程（默认200）
example:
```python Spider_of_t66y.py -c 1 -s 1 -e 2 -m 300```
```python Spider_of_t66y.py -h```
# 友情提醒
注意身体
