import jimi

class _webTrigger(jimi.plugin._plugin):
    version = 0.11

    def install(self):
        jimi.model.registerModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
        jimi.model.registerModel("webTrigger","_webTrigger","_trigger","plugins.webTrigger.models.trigger")
        jimi.model.registerModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        return True

    def uninstall(self):
        jimi.model.deregisterModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
        jimi.model.deregisterModel("webTrigger","_webTrigger","_trigger","plugins.webTrigger.models.trigger")
        jimi.model.deregisterModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 0.11:
            jimi.model.registerModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
            jimi.model.registerModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        return True
