from . import comments_bp


@comments_bp.route('/comments')
def comments_project():
    return 'comments_project'
