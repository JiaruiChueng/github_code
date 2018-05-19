import xadmin
from .models import Post, Category, Tag
from xadmin import views

class PostAdmin(object):
    '''文章'''
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin 也注册进来
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)

class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '豆奶笔记后台管理'
    # 修改footer
    site_footer = '蜀ICP备18007902号-1'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
