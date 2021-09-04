import time

import jimi

from plugins.webTrigger.models import webTrigger

class _webTrigger(jimi.trigger._trigger):
    icon = str()
    formData = list()
    limit = 10

    def check(self):
        events = []
        bulkClass = jimi.db._bulk()
        webTriggerEvents = webTrigger._webTriggerEvent().getAsClass(query={ "webTriggerID" : self._id, "runTime" : 0 },limit=self.limit)["results"]
        for event in webTriggerEvents:
            event.runtime = time.time()
            event.bulkUpdate(["runTime"],bulkClass)
            events.append(event.formResult)
            events[-1]["webTriggerExecutionID"] = event.webTriggerExecutionID
        bulkClass.bulkOperatonProcessing()
        self.result["events"] = events