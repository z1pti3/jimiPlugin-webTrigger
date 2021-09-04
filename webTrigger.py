import jimi

class _webTrigger(jimi.plugin._plugin):
    version = 0.12

    def install(self):
        jimi.model.registerModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
        jimi.model.registerModel("webTrigger","_webTrigger","_trigger","plugins.webTrigger.models.trigger")
        jimi.model.registerModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        jimi.model.registerModel("webTriggerEvent","_webTriggerEvent","_document","plugins.webTrigger.models.webTrigger")
        return True

    def uninstall(self):
        jimi.model.deregisterModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
        jimi.model.deregisterModel("webTrigger","_webTrigger","_trigger","plugins.webTrigger.models.trigger")
        jimi.model.deregisterModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        jimi.model.deregisterModel("webTriggerEvent","_webTriggerEvent","_document","plugins.webTrigger.models.webTrigger")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 0.11:
            jimi.model.registerModel("webTriggerOutput","_webTriggerOutput","_document","plugins.webTrigger.models.webTrigger")
            jimi.model.registerModel("webTriggerAddOutput","_webTriggerAddOutput","_action","plugins.webTrigger.models.action")
        if self.version < 0.12:
            jimi.model.registerModel("webTriggerEvent","_webTriggerEvent","_document","plugins.webTrigger.models.webTrigger")
        return True
