# GameScript  不思议迷宫


### 生成依赖文件：
pip freeze > requirements.txt 
### 批量安装依赖（先设置源下载才快）
pip install -r requirements.txt


### 设置源-解决pip速度慢的问题：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip config set install.trusted-host mirrors.aliyun.com


### 临时使用源：
pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple


### pip国内镜像源：
阿里云	http://mirrors.aliyun.com/pypi/simple/
中国科技大学 	https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣	 http://pypi.douban.com/simple
Python官方	 https://pypi.python.org/simple/
v2ex	 http://pypi.v2ex.com/simple/
中国科学院 	http://pypi.mirrors.opencas.cn/simple/
清华大学	 https://pypi.tuna.tsinghua.edu.cn/simple/

