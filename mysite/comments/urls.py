from django.urls import path

from . import views

# comments アプリケーション内のサイト URL を管理
# URL のうち <> で囲まれた部分は views に変数として引き渡される。
# つけた name はあらゆる場所で URL 文字列の変わりとして使える
app_name = 'comments'
urlpatterns = [
    # index
    path('', views.IndexView.as_view(), name='index'),

    # theme contribution
    path('theme-contribution/', views.ThemeContributionView, name='theme-contribution'),
    path('theme-contribution/contribute/', views.theme_contribute, name='theme-contribute'),
    
    # theme
    path('theme/<int:theme_id>/', views.ThemeView, name='theme'),
    path('theme/<int:theme_id>/contribute/', views.comment_contribute, name='comment-contribute'),
]