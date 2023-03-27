<?php
/**
 * This option name will be used later when we set up the options
 * for the front end theme customizer.
 */

function optionsframework_option_name() {

	$optionsframework_settings = get_option('optionsframework');
	
	$optionsframework_settings['id'] = 'impresa';
	update_option('optionsframework', $optionsframework_settings);
}

/**
 * Defines an array of options that will be used to generate the settings page and be saved in the database.
 * When creating the "id" fields, make sure to use all lowercase and no spaces.
 */

function optionsframework_options() {
	
	// Background Defaults
	$upgrade_message = __('Only available in premium version', 'impresa');
	

	$options[] = array( "name" => __('General', 'impresa'),
		"type" => "heading" );
		
	$options['favicon_uploader'] = array(
		"name" => __('Add favicon', 'impresa'),
		"desc" => __('Upload your favicon', 'impresa'),
		"id" => "favicon_uploader",
		"type" => "upload" );	
	
	$options['logo_uploader'] = array(
		"name" => __('Logo Upload', 'impresa'),
		"desc" =>  __('Upload your logo', 'impresa'),
		"id" => "logo_uploader",
		"type" => "upload" );
    
    $options['icon_iphone'] = array(
		"name" => __('iPhone icon', 'impresa'),
		"desc" =>  __('Apple touch icon iphone (57x57 px)', 'impresa'),
		"id" => "icon_iphone",
		"type" => "upload" );
	
	$options['icon_ipad'] = array(
		"name" => __('iPad icon', 'impresa'),
		"desc" =>  __('Apple touch icon ipad (76x76 px)', 'impresa'),
		"id" => "icon_ipad",
		"type" => "upload" );
	
	$options['icon_iphone_retina'] = array(
		"name" => __('iPhone retina icon', 'impresa'),
		"desc" =>  __('Apple touch icon iphone retina (120x120 px)', 'impresa'),
		"id" => "icon_iphone_retina",
		"type" => "upload" );
	
	$options['icon_ipad_retina'] = array(
		"name" => __('iPad retina icon', 'impresa'),
		"desc" =>  __('Apple touch icon ipad retina (152x152 px)', 'impresa'),
		"id" => "icon_ipad_retina",
		"type" => "upload" );
	
	$options['win_tile_image'] = array(
		"name" => __('Windows 8 pinned image', 'impresa'),
		"desc" =>  __('Pinned site Windows 8 (144x144 px)', 'impresa'),
		"id" => "win_tile_image",
		"type" => "upload" );
	
	$options['win_tile_color'] = array(
		"name" => __('Windows 8 pinned image color', 'impresa'),
		"desc" =>  __('Pinned site Windows 8 color', 'impresa'),
		"id" => "win_tile_color",
		"type" => "color" );

	
	$options[] = array(
		'name' => __('Meta Slider', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array( "name" => __('Style', 'impresa'),
		"type" => "heading" );
	
	$options[] = array(
		'name' => __('Header background', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Menu background color', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');;
			
	$options[] = array(
		'name' => __('Link color', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Link color on hover', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Footer background', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array( "name" => __('Blog &amp; Pages', 'impresa'),
		"type" => "heading" );
	
	$options[] = array(
		'name' => __('Pages comments', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Show blog and archive featured image', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Show post featured image', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Display post meta', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
		
	$options[] = array(
		'name' => __('Index sidebar', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Post sidebar', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array( "name" => __('Footer', 'impresa'),
		"type" => "heading" );
		
	$options[] = array(
		'name' => __('Footer text', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array(
		'name' => __('Display credits link', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
	
	$options[] = array( "name" => __('Social', 'impresa'),
		"type" => "heading" );
			
	$options[] = array(
		'name' => __('Facebook url', 'base'),
		'desc' => __('Add the url of your Facebook page', 'base'),
		'id' => 'facebook_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Twitter url', 'base'),
		'desc' => __('Add the url of your Twitter page', 'base'),
		'id' => 'twitter_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Google plus url', 'base'),
		'desc' => __('Add the url of your Google Plus page', 'base'),
		'id' => 'google_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Pinterest url', 'base'),
		'desc' => __('Add the url of your Pinterest page', 'base'),
		'id' => 'pinterest_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Tumblr url', 'base'),
		'desc' => __('Add the url of your Tumblr page', 'base'),
		'id' => 'tumblr_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Instagram url', 'base'),
		'desc' => __('Add the url of your Instagram page', 'base'),
		'id' => 'instagram_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Linkedin url', 'base'),
		'desc' => __('Add the url of your Linkedin page', 'base'),
		'id' => 'linkedin_url',
		'std' => '',
		'type' => 'text');
		
	$options[] = array(
		'name' => __('Dribbble url', 'base'),
		'desc' => __('Add the url of your Dribbble page', 'base'),
		'id' => 'dribbble_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Vimeo url', 'base'),
		'desc' => __('Add the url of your Vimeo page', 'base'),
		'id' => 'vimeo_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('Youtube url', 'base'),
		'desc' => __('Add the url of your Youtube page', 'base'),
		'id' => 'youtube_url',
		'std' => '',
		'type' => 'text');
	
	$options[] = array(
		'name' => __('RSS url', 'base'),
		'desc' => __('Add the url of your RSS', 'base'),
		'id' => 'rss_url',
		'std' => '',
		'type' => 'text');
		
	$options[] = array( "name" => __('Advanced', 'impresa'),
		"type" => "heading" );	
	
	$options[] = array(
		'name' => __('Custom css', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');

	$options[] = array(
		'name' => __('Footer code', 'impresa'),
		'desc' => $upgrade_message,
		'type' => 'info');
		
return $options;
}

/**
 * Front End Customizer
 *
 * WordPress 3.4 Required
 */

add_action( 'customize_register', 'options_theme_customizer_register' );

function options_theme_customizer_register($wp_customize) {

	/**
	 * This is optional, but if you want to reuse some of the defaults
	 * or values you already have built in the options panel, you
	 * can load them into $options for easy reference
	 */
	 
	$options = optionsframework_options();
	
	/* Logo upload */

	$wp_customize->add_section( 'options_theme_customizer_logo', array(
		'title' => __( 'Logo Upload', 'impresa' ),
		'priority' => 110
	) );
	
	$wp_customize->add_setting( 'options_theme_customizer[logo_uploader]', array(
		'type' => 'option',
        'sanitize_callback' => 'esc_url_raw'
	) );
	
	$wp_customize->add_control( new WP_Customize_Image_Control( $wp_customize, 'logo_uploader', array(
		'label' => $options['logo_uploader']['name'],
		'section' => 'options_theme_customizer_logo',
		'settings' => 'options_theme_customizer[logo_uploader]'
	) ) );	
	
	
	/* Add favicon */

	$wp_customize->add_section( 'options_theme_customizer_favicon', array(
		'title' => __( 'Favicon', 'impresa' ),
		'priority' => 110
	) );
	
	$wp_customize->add_setting( 'options_theme_customizer[favicon_uploader]', array(
		'type' => 'option',
        'sanitize_callback' => 'esc_url_raw'

	) );
	
	$wp_customize->add_control( new WP_Customize_Image_Control( $wp_customize, 'favicon_uploader', array(
		'label' => $options['favicon_uploader']['name'],
		'section' => 'options_theme_customizer_favicon',
		'settings' => 'options_theme_customizer[favicon_uploader]'
	) ) );	
}


add_action('optionsframework_after','optionscheck_display_sidebar', 100);

function optionscheck_display_sidebar() { ?>
    <div class="metabox-holder upgrade">
        <div class="postbox">
            <h3><?php echo __('Upgrade to premium', "impresa"); ?></h3>
                <div class="inside">
                    <p><?php echo __('Upgrade to the premium version to get access to advanced options and priority support.', "impresa"); ?></p>
                    <a title="Upgrade to premium version" href="http://www.iograficathemes.com/downloads/big-impresa-premium/" target="_blank">
                    <span class="upgrade-button">Upgrade to premium</span>
                    </a>
					<p><?php echo __('We offer a 7 day full refund if you are not happy with your purchase.',  "impresa"); ?></p>
                </div>
        </div>
        <div class="inside">
                    <h3><?php echo __('Iografica Themes', "impresa"); ?></h3>
                    <a title="Facebook" href="https://www.facebook.com/iograficathemes" target="_blank">
                    <span class="facebook"><?php echo __('Facebook', "impresa"); ?></span>
                    </a>
                    <?php echo __(' | ', "impresa"); ?>
					<a title="Twitter" href="https://twitter.com/iograficathemes" target="_blank">
                    <span class="twitter"><?php echo __('Twitter', "impresa"); ?></span>
                    </a>
                    <?php echo __(' | ', "impresa"); ?>
					<a title="Google Plus" href="http://plus.google.com/111064256285067685536" target="_blank">
                    <span class="website"><?php echo __('Google Plus', "impresa"); ?></span>
                    </a>
                    <?php echo __(' | ', "impresa"); ?>
					<a title="Iografica Themes" href="http://www.iograficathemes.com" target="_blank">
                    <span class="website"><?php echo __('Website', "impresa"); ?></span>
                    </a>
                </div>
    </div>
    </div>
<?php }