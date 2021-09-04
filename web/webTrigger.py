from flask import Blueprint, render_template, redirect, send_from_directory
from flask import current_app as app
from pathlib import Path
import json

import jimi

from plugins.webTrigger.models import trigger
from plugins.webTrigger.models import webTrigger

pluginPages = Blueprint('webTriggerPages', __name__, template_folder="templates")

@pluginPages.route('/includes/<file>')
def custom_static(file):
    return send_from_directory(str(Path("plugins/webTrigger/web/includes")), file)

@pluginPages.route("/",methods=["GET"])
def mainPage():
    triggers = trigger._webTrigger().query(sessionData=jimi.api.g.sessionData,query={},fields=["_id","name","icon"])["results"]
    return render_template("webTrigger.html", CSRF=jimi.api.g.sessionData["CSRF"],  triggers=triggers)

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

@pluginPages.route("/<webTriggerID>/",methods=["POST"])
def postForm(webTriggerID):
    try:
        webTriggerItem = trigger._webTrigger().query(sessionData=jimi.api.g.sessionData,id=webTriggerID,fields=["_id","name","formData"])["results"][0]
        data = json.loads(jimi.api.request.data)
        formData = {}
        for field in webTriggerItem["formData"]:
            if field["schema_item"] in data:
                formData[field["schema_item"]] = data[field["schema_item"]]
            else:
                if field["type"] == "input":
                    formData[field["schema_item"]] = ""
                elif field["type"] == "json-input":
                    formData[field["schema_item"]] = {}
                elif field["type"] == "checkbox":
                    formData[field["schema_item"]] = False
                elif field["type"] == "dropdown":
                    formData[field["schema_item"]] = ""
                else:
                    formData[field["schema_item"]] = None
        webTriggerExecutionID = webTrigger._webTriggerEvent().new(webTriggerItem["acl"],webTriggerItem["_id"],formData)
        return { "result" : { "webTriggerExecutionID" : webTriggerExecutionID } }, 200
    except:
        return {}, 403

@pluginPages.route("/<webTriggerID>/<webTriggerExecutionID>/",methods=["GET"])
def getTriggerOutput(webTriggerID,webTriggerExecutionID):
    return render_template("webTriggerOutput.html", CSRF=jimi.api.g.sessionData["CSRF"])

@pluginPages.route("/<webTriggerID>/<webTriggerExecutionID>/data/",methods=["GET"])
def getTriggerOutputData(webTriggerID,webTriggerExecutionID):
    try:
        webTriggerEvent = webTrigger._webTriggerEvent().query(sessionData=jimi.api.g.sessionData,query={ "webTriggerID" : webTriggerID, "webTriggerExecutionID" : webTriggerExecutionID },fields=["_id","runTime"])["results"][0]
        started = False
        if webTriggerEvent["runTime"] > 0:
            started = True
        webTriggerOutput = webTrigger._webTriggerOutput().query(query={ "webTriggerID" : webTriggerID, "webTriggerExecutionID" : webTriggerExecutionID },fields=["_id","outputData"])["results"]
        return { "result" : { "started" : started, "output" : webTriggerOutput } },200
    except:
        return {}, 403