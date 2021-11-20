import jimi

from plugins.webTrigger.models import webTrigger

class _webTriggerAddOutput(jimi.action._action):
    output_data = str()
    webTriggerID = str()
    webTriggerExecutionID = str()
    outputType = "content"

    def doAction(self,data):
        try:
            if self.webTriggerID:
                webTriggerID = jimi.helpers.evalString(self.webTriggerID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            else:
                webTriggerID = data["flowData"]["event"]["webTriggerID"]
            if self.webTriggerExecutionID:
                webTriggerExecutionID = jimi.helpers.evalString(self.webTriggerExecutionID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            else:
                webTriggerExecutionID = data["flowData"]["event"]["webTriggerExecutionID"]
        except:
            return { "result" : True, "rc" : 1, "msg" : "webTriggerExecutionID not found"  }

        try:
            output_data = jimi.helpers.evalString(self.output_data,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
            outputDict = {"type":self.outputType,"content":output_data}
            webTrigger._webTriggerOutput().new(self.acl,webTriggerID,webTriggerExecutionID,outputDict)
            return { "result" : True, "rc" : 0  }
        except:
            return { "result" : True, "rc" : 2, "msg" : "Error adding webTrigger output"  }