#安装django
project_name=project
app_name=freedom
	django-admin startproject $project_name
	python run.py startapp $app_name
	# ......
	python run.py makemigrations
	python run.py migrate

	python run.py runserver ip:port
	python run.py createsuperuser # 按提示输入用户名、邮箱、密码