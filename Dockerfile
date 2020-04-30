
FROM python:3.7.4

MAINTAINER name 931977674@qq.com

# 代码添加到code文件夹
ADD ./clsq_spider /code

# 设置code文件夹是工作目录
WORKDIR /code

# 安装相关依赖
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 执行main方法
CMD ["python", "/code/main.py"]