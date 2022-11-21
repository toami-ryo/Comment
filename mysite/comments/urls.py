from django.urls import path

from . import views

# comments アプリケーション内のサイト URL を管理
# URL のうち <> で囲まれた部分は views に変数として引き渡される。
# つけた name はあらゆる場所で URL 文字列の変わりとして使える
app_name = 'comments'
urlpatterns = [
    # ex: /comments/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:theme_id>/', views.CommentsView, name='comments'),
    path('<int:theme_id>/contribute/', views.contribute, name='contribute')
]