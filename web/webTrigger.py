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
    triggers = trigger._webTrigger().query(sessionData=jimi.api.g.sessionData,query={},fields=["_id","name","icon"])["results"]
    return render_template("webTrigger.html", triggers=triggers)

@pluginPages.route("/<webTriggerID>/",methods=["GET"])
def getForm(webTriggerID):
    try:
        webTrigger = trigger._webTrigger().query(sessionData=jimi.api.g.sessionData,id=webTriggerID,fields=["_id","name","formData"])["results"][0]
        # Process and correct formData
        for field in webTrigger["formData"]:
            field["schemaitem"] = field["schema_item"]
            if field["type"] == "input":
                field["textbox"] = ""
            elif field["type"] == "json-input":
                field["textbox"] = {}
            elif field["type"] == "checkbox":
                field["checked"] = False
            elif field["type"] == "group-checkbox":
                field["checked"] = False
            elif field["type"] == "dropdown":
                field["current"] = ""
            field["tooltip"] = field["description"]
        return { "result" : webTrigger }
    except:
        return {}, 403

