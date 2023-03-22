define([
    'base/js/notificationarea'
], function(notificationarea) {
    "use strict";
    var NotificationArea = notificationarea.NotificationArea;
    
    var EditorNotificationArea = function(selector, options) {
        NotificationArea.apply(this, [selector, options]);
    }
    
    EditorNotificationArea.prototype = Object.create(NotificationArea.prototype);
    
    /**
     * Initialize the default set of notification widgets.
     *
     * @method init_notification_widgets
     */
    EditorNotificationArea.prototype.init_notification_widgets = function () {
        var that = this;
        var savew = this.new_notification_widget('save');
        
        this.events.on("file_saved.Editor", function() {
            savew.set_message("File saved", 2000);
        });
    };
    

    return {EditorNotificationArea: EditorNotificationArea};
});
