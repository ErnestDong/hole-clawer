# 树洞爬虫
## 使用方式
### 获得你的 token 
写入 [app.py](./app.py) 中相应位置
### 安装依赖
数据持久化采用 [sqlite](https://www.sqlite.org/index.html)，请自行安装
```shell
# 我使用
poetry install
# 或者
pip install -r requirements.txt
```
### 开始跑
根据想要爬的数量并在 [app.py](./app.py) 中选择性注释
```shell
python app.py
```
会把所有结果打到 log 文件夹下

## 未来计划

无法搞定验证码，会挤垮服务器（？），暂时不更新
