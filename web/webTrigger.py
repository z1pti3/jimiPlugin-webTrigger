from flask import Blueprint, render_template, redirect, send_from_directory
from flask import current_app as app
from pathlib import Path

import jimi

from plugins.webTrigger.models import webTrigger

pluginPages = Blueprint('webTriggerPages', __name__, template_folder="templates")

@pluginPages.route('/includes/<file>')
def custom_static(file):
    return send_from_directory(str(Path("plugins/webTrigger/web/includes")), file)

@pluginPages.route("/",methods=["GET"])
def __public__mainPage():
    triggers = webTrigger._webTrigger().query({})["results"]
    return render_template("webTrigger.html", triggers=triggers)
