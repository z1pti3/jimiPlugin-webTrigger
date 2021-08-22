from flask import Blueprint, render_template, redirect, send_from_directory
from flask import current_app as app
from pathlib import Path

import jimi

from plugins.webTrigger.models import trigger

pluginPages = Blueprint('webTriggerPages', __name__, template_folder="templates")

@pluginPages.route('/includes/<file>')
def custom_static(file):
    return send_from_directory(str(Path("plugins/webTrigger/web/includes")), file)

@pluginPages.route("/",methods=["GET"])
def mainPage():
    triggers = trigger._webTrigger().query(sessionData=jimi.api.g.sessionData,query={},fields=["_id","name","icon","formData"])["results"]
    return render_template("webTrigger.html", triggers=triggers)
