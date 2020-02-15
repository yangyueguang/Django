#安装django
cd ..
project_name=projects
app_name=apps
ip='127.0.0.1'
port=8000
pip3 install -r requires.txt
django-admin startproject $project_name
cd $project_name
python3 manager.py startapp $app_name
	# ......
python3 manager.py makemigrations $app_name
python3 manager.py migrate

python3 manager.py runserver $ip:$port
python3 manager.py createsuperuser # 按提示输入用户名、邮箱、密码 admin 123456

# about celery
python3 manager.py migrate
# =================================================
# 部署 使用wsgi方式
pip freeze > requires.txt
通过ftp软件将开发好的项目上传到此服务器的某个目录
安装并创建虚拟环境，如果已有则跳过此步
sudo apt-get install python-virtualenv
sudo easy_install virtualenvwrapper
mkvirtualenv [虚拟环境名称]
在虚拟环境上工作，安装所有需要的包
workon [虚拟环境名称]
pip install -r plist.txt
更改settings.py文件
DEBUG = False
ALLOW_HOSTS=['*',]表示可以访问服务器的ip
pip install uwsgi
#启动：
uwsgi --ini uwsgi.ini
#停止：
uwsgi --stop uwsgi.pid
#重启：
uwsgi --reload uwsgi.pid

#=========================================
# 部署使用nginx方式
sudo yum install nginx
tar -xzvf nginx-1.6.3.tar.gz
./configure
make
sudo make install
默认安装到/usr/local/nginx目录，进入此目录执行命令
查看版本：sudo sbin/nginx -v
启动：sudo sbin/nginx
停止：sudo sbin/nginx -s stop
重启：sudo sbin/nginx -s reload
通过浏览器查看nginx运行结果
指向uwsgi项目：编辑conf/nginx.conf文件
sudo conf/nginx.conf

在server下添加新的location项，指向uwsgi的ip与端口
location / {
    include uwsgi_params;将所有的参数转到uwsgi下
    uwsgi_pass uwsgi的ip与端口;
}
修改uwsgi.ini文件，启动socket，禁用http
重启nginx、uwsgi
在浏览器中查看项目，发现静态文件加载不正常，接下来解决静态文件的问题
静态文件
静态文件一直都找不到，现在终于可以解决了
所有的静态文件都会由nginx处理，不会将请求转到uwsgi
配置nginx的静态项，打开conf/nginx.conf文件，找到server，添加新location
location /static {
    alias /var/www/test5/static/;
}
在服务器上创建目录结构“/var/www/test5/”
修改目录权限
sudo chmod 777 /var/www/test5
创建static目录，注意顺序是先分配权限，再创建目录
mkdir static
最终目录结构如下图：
static

修改settings.py文件
STATIC_ROOT='/var/www/test5/static/'
STATIC_URL='/static/'
收集所有静态文件到static_root指定目录：python manage.py collectstatic
重启nginx、uwsgi