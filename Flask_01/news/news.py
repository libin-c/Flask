from . import news_bp

@news_bp.route('/news')
def news_project():
    return 'news_project'

