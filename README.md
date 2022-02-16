# 树洞爬虫
## 使用方式
### 获得你的 token 
写入 [app.py](./app.py) 中相应位置
### 安装依赖
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

- TODO 数据持久化到数据库或 excel 中
- TODO 改为多进程加快速度
- TODO 人机验证（目前只遇到一次，大意了没有闪验证通过了）
