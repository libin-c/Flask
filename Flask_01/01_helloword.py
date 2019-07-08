from flask import Flask
import  os
# static_url_path 设置访问的静态路由
# static_folder 设置static静态文件路径 默认static
#  template_folder设置template模板路径 默认template
app = Flask(__name__, static_url_path='/s', static_folder='/static', template_folder='/template')

# 单一配置config的方式
# app.config['SECRET_KEY'] = 'www.baiduo.com'


# 获取 config 的两种方式  和 dict 类似
# 01 app.config.get('SECRET_KEY')
# 02 app.config['SECRET_KEY']

# 01 第一种配置方式 创建类 优点 ：继承复用 ； 缺点：不安全
class DefaultConfig(object):
    MYSQL_CONFIG = 'Flask mysql 1'
    REDIS_CONFIG = 'Flask redis 1'


# app.config.from_object(DefaultConfig)


# 02 第二种配置文件的方式  创建settings 配置文件（可以任何文件） 优点：相对安全 ，单独维护的时候安全；缺点不能继承，而且会暴露配置文件在哪个文件，一般不采用
# 01  silent = True  # 静默处理  出现错误的时候 忽略 不报错  有点类似rm -rf 中的f 没有警告
# 02  silent = False #出现错误的时候报错
# app.config.from_pyfile('settings.py', silent=False)

# 03  第三种是从环境变量中配置
app.config.from_envvar('DEMO')


@app.route('/')
def helloWord():
    print(app.config.get('MYSQL_CONFIG'))
    return "hello  world"


if __name__ == '__main__':
    app.run()
