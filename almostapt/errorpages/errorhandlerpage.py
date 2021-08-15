from flask import Blueprint, render_template

errorpages = Blueprint('errorpages', __name__, template_folder="templates")


@errorpages.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errorpages.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errorpages.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500