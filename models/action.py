import jimi

from plugins.webTrigger.models import webTrigger

class _webTriggerAddOutput(jimi.action._action):
    output_data = str()
    webTriggerID = str()
    webTriggerExecutionID = str()

    def doAction(self,data):
        if self.webTriggerID:
            webTriggerID = jimi.helpers.evalString(self.webTriggerID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        else:
            webTriggerID = data["flowData"]["event"]["webTriggerID"]
        if self.webTriggerExecutionID:
            webTriggerExecutionID = jimi.helpers.evalString(self.webTriggerExecutionID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        else:
            webTriggerExecutionID = data["flowData"]["event"]["webTriggerExecutionID"]

        output_data = jimi.helpers.evalString(self.output_data,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        webTrigger._webTriggerOutput().new(self.acl,webTriggerID,webTriggerExecutionID,output_data)
        return { "result" : True, "rc" : 0  }