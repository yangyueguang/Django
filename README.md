# 这是Django框架
[接口文档](https://my.apipost.cn/doc?project_id=35275#195056)
功能说明
=========================================
[Flask](https://dormousehole.readthedocs.io/en/latest/) Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2 模板引擎。Flask使用BSD授权。
Flask被称为“microframework”，因为它使用简单的核心，用extension增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术
* [部署流程](#部署流程)
* [性能测试](#性能测试)
* [拦截器](#拦截器)
* [会话保持](#会话保持)
* [测试用例](#测试用例)
* [使用方法和注意事项](#使用方法和注意事项)
* [TODO](#TODO)


*************


### 部署流程
1, 将项目clone到本地，  

```angular2
git clone ssh://git@git.datagrand.com:58422/jianzhihua/flask-demo-pro.git <your-project-name>
```

2, 进入项目，删除.git文件夹，并将项目和自己的远程仓库相连

3, 进入虚拟环境, 进入项目根目录下， 执行下列命令安装Python 依赖

```angular2
pip install -r requirements.txt
```

3, 如果是在本地调试，可以执行如下命令(正式环境不要采用这种方式, 会造成阻塞)：
```angular2
cd admin && sh debug.sh
```
3, 如果是在本地调试，也可以执行如下命令(正式环境不要采用这种方式, 会造成阻塞)：
```angular2
python run.py
```
4, 如果是上线部署，执行如下命令, deploy.sh脚本中预留从环境变量中获取端口号, 可以用到docker中
```
cd admin && sh deploy.sh
```



### 性能测试
#### 默认启动方式性能测试
Mac上执行命令安装siege, 并发测试命令。
```angular2
brew install siege
```
采用debug.sh方式启动, 执行如下命令进行测试
```
siege -c 10 -r 10 http://127.0.0.1:5001/demo/test
```
执行结果如下
```
Transactions:		         100 hits
Availability:		      100.00 %
Elapsed time:		     1000.54 secs
Data transferred:	        0.01 MB
Response time:		       95.55 secs
Transaction rate:	        0.10 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        9.55
Successful transactions:         100
Failed transactions:	           0
Longest transaction:	      100.09
Shortest transaction:	       10.01
```
通过测试可以看出，最长的链接等待了100s, 也就是说同时10个并发， 有一个特别倒霉，一直等到最后一刻。 
#### gunicorn启动方式性能测试
采用deploy.sh启动方式性能测试
```
siege -c 10 -r 10 http://127.0.0.1:5001/demo/test
```
执行结果如下
```
Transactions:		         100 hits
Availability:		      100.00 %
Elapsed time:		      100.05 secs
Data transferred:	        0.01 MB
Response time:		       10.00 secs
Transaction rate:	        1.00 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		       10.00
Successful transactions:         100
Failed transactions:	           0
Longest transaction:	       10.01
Shortest transaction:	       10.00
```
从上面的执行结果对比中可以看出，最长等待时间是10s，可见10个并发请求时，10个请求几乎是被同时处理的

#### 拦截器
Flask 是一个轻量级的框架， 如果需要拦截器，使用@app.before_request等。

#### 会话保持
Flask 中可以采用装饰器，在缓存redis中判定用户是否登陆或者存在, 参考代码如下：
```angular2
from functools import wraps
from flask import session, abort
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not 'user' in session:
            abort(401)
        return func(*args, **kwargs)
    return decorated_function
```

#### 使用方法和注意事项 
Flask 是一款很轻量级的框架， 组件非常的丰富。相比于Tornado 框架由于Flask采用的是开多进程
提高并发的方式，所以Flask更适合用来操作数据库等延时性比较高的操作。就算一个进程出现卡顿，
别的进程依然可以提供正常的服务。
* 1， 在routes.py文件中增加路由映射。
* 2， 添加路由映射文件， 增加路由映射的Handler。
* 3， 所有的业务服务写在service中， Handler中只写跟该请求有关的主流程。
* 5， 可以在Flask 项目链接MySQL， Oracle 等数据库不会出现主线程卡死导致全站卡死。
* 6， 如果需要新建链接， 比如链接kafka等， 可以在app文件夹下的__init__.py文件中添加
一个句柄kafkaproducer 需要用到的地方引用一下即可。



#### 测试用例
本demo的测试用例在/test 路径下， 采用unittest的方式进行单元测试。

#### TODO

* Flask JWT 认证

* Flask模板渲染

* Flask异步任务处理(celery方式)




