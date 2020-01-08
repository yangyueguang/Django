# 这是Django框架
[接口文档](https://my.apipost.cn/doc?project_id=35275#195056)

功能说明
*************
### 部署流程
1, 将项目clone到本地，  

```angular2
git clone ssh://git@git.datagrand.com:58422/jianzhihua/flask-demo-pro.git <your-project-name>
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
