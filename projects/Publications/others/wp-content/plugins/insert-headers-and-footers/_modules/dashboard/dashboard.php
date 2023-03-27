<?php
/**
* Dashboard Widget
*/
class WPBeginnerDashboardWidget {     
	/**
	* Constructor
	*
	* @param object $plugin Plugin Object (name, displayName, version, folder, url)
	*/
	function __construct($plugin) {
		// Plugin Details
        $this->dashboard = $plugin;
        $this->dashboardURL = WP_PLUGIN_URL.'/'.str_replace(basename( __FILE__),"",plugin_basename(__FILE__));

		// Hooks
		add_action('admin_enqueue_scripts', array(&$this, 'adminScriptsAndCSS'));
		add_action('wp_dashboard_setup', array(&$this, 'dashboardWidget'));
		add_action('wp_network_dashboard_setup', array(&$this, 'dashboardWidget'));	
	} 
	
	/**
    * Register and enqueue dashboard CSS
    */
    function adminScriptsAndCSS() {    
    	// CSS
    	// This will only enqueue once, despite this hook being called by up to several plugins,
    	// as we have set a single, distinct name
        wp_enqueue_style('wpbeginner', $this->dashboardURL.'css/admin.css'); 
    } 	
    
	/**
    * Adds a dashboard widget to output WPBeginner RSS
    *
    * Checks if another WPBeginner plugin has already created this widget - if so, doesn't duplicate it
    */
    function dashboardWidget() {
    	global $wp_meta_boxes;
    	
    	if (isset($wp_meta_boxes['dashboard']['normal']['core']['wpbeginner'])) return; // Another plugin has already registered this widget
    	wp_add_dashboard_widget('wpbeginner', __('Latest from WPBeginner', $this->dashboard->name), array(&$this, 'outputDashboardWidget'));
    }
    
    /**
    * Called by dashboardWidget(), includes dashboard.php to output the Dashboard Widget
    */
    function outputDashboardWidget() {
    	$result = wp_remote_get('http://wpbeginner.com/feed/');
    	if (!is_wp_error($result)) {
	    	if ($result['response']['code'] == 200) {
	    		$xml = simplexml_load_string($result['body']);
	    		$rssPosts = $xml->channel;
	    	}
	    	
	    	include_once(WP_PLUGIN_DIR.'/'.$this->dashboard->name.'/_modules/dashboard/views/dashboard.php');
    	} else {
    		include_once(WP_PLUGIN_DIR.'/'.$this->dashboard->name.'/_modules/dashboard/views/dashboard-nodata.php');
    	}
    }
}
?>