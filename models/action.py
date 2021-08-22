import jimi

from plugins.webTrigger.models import webTrigger

class _webTriggerAddOutput(jimi.action._action):
    output_data = str()

    def doAction(self,data):
        output_data = jimi.helpers.evalString(self.output_data,{"data" : data["flowData"], "eventData" : data["eventData"]})
        webTrigger._webTriggerOutput().new(self.acl,data["persistentData"]["plugin"]["webTrigger"]["webTriggerID"],data["persistentData"]["plugin"]["webTrigger"]["webTriggerExecutionID"],output_data)
        return { "result" : True, "rc" : 0  }