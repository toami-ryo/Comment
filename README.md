# Comment
### 目標  
掲示板をつくってみる
\
\
python 3.9.13  
Django 4.1.3
\
\
\
1  
setting.py の  
from .settings_local import *
を削除し、  
SECRET_KEY = 'xxxx'  
を書き加える。'xxxx' は再生成したシークレットキー。  
参考：https://chigusa-web.com/blog/django-secret/

2  
Comment/mysite/ に移動し、sqlite ファイルをつくる  
python manage.py migrate  

3  
django の開発用サーバーを起動  
python mysite/manage.py runserver

4  
ブラウザでアクセス
http://127.0.0.1:8000/comments/