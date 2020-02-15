#安装django
cd ..
project_name=projects
app_name=apps
django-admin startproject $project_name
python manager.py startapp $app_name
	# ......
python manager.py makemigrations
python manager.py migrate

python manager.py runserver ip:port
python manager.py createsuperuser # 按提示输入用户名、邮箱、密码