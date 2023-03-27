<?php
/**
* Plugin Name: Insert Headers and Footers
* Plugin URI: http://www.wpbeginner.com/
* Version: 1.3.3
* Author: WPBeginner
* Author URI: http://www.wpbeginner.com/
* Description: Allows you to insert code or text in the header or footer of your WordPress blog
* License: GPL2
*/

/*  Copyright 2014 WPBeginner

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License, version 2, as 
    published by the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

/**
* Insert Headers and Footers Class
*/
class InsertHeadersAndFooters {
	/**
	* Constructor
	*/
	public function __construct() {

		// Plugin Details
        $this->plugin               = new stdClass;
        $this->plugin->name         = 'insert-headers-and-footers'; // Plugin Folder
        $this->plugin->displayName  = 'Insert Headers and Footers'; // Plugin Name
        $this->plugin->version      = '1.3.3';
        $this->plugin->folder       = plugin_dir_path( __FILE__ );
        $this->plugin->url          = plugin_dir_url( __FILE__ );

        // Dashboard Submodule
        if (!class_exists('WPBeginnerDashboardWidget')) {
			require_once($this->plugin->folder.'/_modules/dashboard/dashboard.php');
		}
		$this->dashboard = new WPBeginnerDashboardWidget($this->plugin); 
		
		// Hooks
		add_action('admin_init', array(&$this, 'registerSettings'));
        add_action('admin_menu', array(&$this, 'adminPanelsAndMetaBoxes'));
        
        // Frontend Hooks
        add_action('wp_head', array(&$this, 'frontendHeader'));
		add_action('wp_footer', array(&$this, 'frontendFooter'));
	}
	
	/**
	* Register Settings
	*/
	function registerSettings() {
		register_setting($this->plugin->name, 'ihaf_insert_header', 'trim');
		register_setting($this->plugin->name, 'ihaf_insert_footer', 'trim');
	}
	
	/**
    * Register the plugin settings panel
    */
    function adminPanelsAndMetaBoxes() {
    	add_submenu_page('options-general.php', $this->plugin->displayName, $this->plugin->displayName, 'manage_options', $this->plugin->name, array(&$this, 'adminPanel'));
	}
    
    /**
    * Output the Administration Panel
    * Save POSTed data from the Administration Panel into a WordPress option
    */
    function adminPanel() {
    	// Save Settings
        if (isset($_POST['submit'])) {
        	// Check nonce
        	if (!isset($_POST[$this->plugin->name.'_nonce'])) {
	        	// Missing nonce	
	        	$this->errorMessage = __('nonce field is missing. Settings NOT saved.', $this->plugin->name);
        	} elseif (!wp_verify_nonce($_POST[$this->plugin->name.'_nonce'], $this->plugin->name)) {
	        	// Invalid nonce
	        	$this->errorMessage = __('Invalid nonce specified. Settings NOT saved.', $this->plugin->name);
        	} else {        	
	        	// Save
	    		update_option('ihaf_insert_header', $_POST['ihaf_insert_header']);
	    		update_option('ihaf_insert_footer', $_POST['ihaf_insert_footer']);
				$this->message = __('Settings Saved.', $this->plugin->name);
			}
        }
        
        // Get latest settings
        $this->settings = array(
        	'ihaf_insert_header' => stripslashes(get_option('ihaf_insert_header')),
        	'ihaf_insert_footer' => stripslashes(get_option('ihaf_insert_footer')),
        );
        
    	// Load Settings Form
        include_once(WP_PLUGIN_DIR.'/'.$this->plugin->name.'/views/settings.php');  
    }
    
    /**
	* Loads plugin textdomain
	*/
	function loadLanguageFiles() {
		load_plugin_textdomain($this->plugin->name, false, $this->plugin->name.'/languages/');
	}
	
	/**
	* Outputs script / CSS to the frontend header
	*/
	function frontendHeader() {
		$this->output('ihaf_insert_header');
	}
	
	/**
	* Outputs script / CSS to the frontend footer
	*/
	function frontendFooter() {
		$this->output('ihaf_insert_footer');
	}
	
	/**
	* Outputs the given setting, if conditions are met
	*
	* @param string $setting Setting Name
	* @return output
	*/
	function output($setting) {
		// Ignore admin, feed, robots or trackbacks
		if (is_admin() OR is_feed() OR is_robots() OR is_trackback()) {
			return;
		}
		
		// Get meta
		$meta = get_option($setting);
		if (empty($meta)) {
			return;
		}	
		if (trim($meta) == '') {
			return;
		}
		
		// Output
		echo stripslashes($meta);
	}
}
		
$ihaf = new InsertHeadersAndFooters();
?>