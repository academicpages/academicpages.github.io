<?php
/**
 * impresa functions and definitions
 */
if ( ! function_exists( 'impresa_setup' ) ) :

/**
* Sets up theme defaults and registers support for various WordPress features.
*
* Note that this function is hooked into the after_setup_theme hook, which
* runs before the init hook. The init hook is too late for some features, such
* as indicating support for post thumbnails.
*/
function impresa_setup() {
    
/**
 * Set the content width based on the theme's design and stylesheet.
 */
if ( ! isset( $content_width ) )
$content_width = 700; /* pixels */
		
/*
* Make theme available for translation.
* Translations can be filed in the /languages/ directory.
* If you're building a theme based on this theme, use a find and replace
* to change 'impresa' to the name of your theme in all the template files
*/
load_theme_textdomain( 'impresa', get_template_directory() . '/languages' );

// Add default posts and comments RSS feed links to head.
add_theme_support( 'automatic-feed-links' );

/*
* Enable support for Post Thumbnails on posts and pages.
*
* @link http://codex.wordpress.org/Function_Reference/add_theme_support#Post_Thumbnails
*/
add_theme_support( 'post-thumbnails' );

// This theme uses wp_nav_menu() in one location.
register_nav_menus( array(
	'primary' => __( 'Primary Menu', 'impresa' ),
) );

// Enable support for Post Formats.
add_theme_support( 'post-formats', array( 'aside', 'image', 'video', 'quote', 'link' ) );
	
// Allows theme developers to link a custom stylesheet file to the TinyMCE visual editor.
function impresa_add_editor_styles() {
    add_editor_style( 'custom-editor-style.css' );
	}
add_action( 'init', 'impresa_add_editor_styles' );
	
// Setup the WordPress core custom background feature.
add_theme_support( 'custom-background', apply_filters( 'impresa_custom_background_args', array(
	'default-color' => 'f9f9f9',
	'default-image' => '',
) ) );

// Enable support for HTML5 markup.
	add_theme_support( 'html5', array( 'comment-list', 'search-form', 'comment-form', ) );
}
endif; // impresa_setup
add_action( 'after_setup_theme', 'impresa_setup' );

/**
 * Register widgetized area and update sidebar with default widgets.
 */
function impresa_widgets_init() {
	register_sidebar( array(
		'name'          => __( 'Sidebar', 'impresa' ),
		'id'            => 'sidebar-1',
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
		
// Area footer 1, located in the footer. Empty by default.
	register_sidebar( array(
		'name' => __( 'First Footer Widget Area', 'impresa' ),
		'id' => 'first-footer-widget-area',
		'description' => __( 'The first footer widget area', 'impresa' ),
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
	
// Area footer 2, located in the footer. Empty by default.
	register_sidebar( array(
		'name' => __( 'Second Footer Widget Area', 'impresa' ),
		'id' => 'second-footer-widget-area',
		'description' => __( 'The second footer widget area', 'impresa' ),
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
	
// Area footer 3, located in the footer. Empty by default.
	register_sidebar( array(
		'name' => __( 'Third Footer Widget Area', 'impresa' ),
		'id' => 'third-footer-widget-area',
		'description' => __( 'The third footer widget area', 'impresa' ),
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
	
// Area footer 4, located in the footer. Empty by default.
	register_sidebar( array(
		'name' => __( 'Fourth Footer Widget Area', 'impresa' ),
		'id' => 'fourth-footer-widget-area',
		'description' => __( 'The fourth footer widget area', 'impresa' ),
			'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
}
add_action( 'widgets_init', 'impresa_widgets_init' );

/**
 * Enqueue scripts and styles.
 */
function impresa_scripts() {
	wp_enqueue_style( 'impresa-style', get_stylesheet_uri() );
	
	wp_enqueue_style( 'impresa-skeleton', get_template_directory_uri().'/css/skeleton.css' );
	
	wp_enqueue_style( 'impresa-layout', get_template_directory_uri().'/css/layout.css' );
    
    wp_enqueue_style( 'impresa-icon', get_template_directory_uri().'/inc/icon/style.css' );

	wp_enqueue_script( 'impresa-navigation', get_template_directory_uri() . '/js/navigation.js', array(), '20120206', true );

	wp_enqueue_script( 'impresa-skip-link-focus-fix', get_template_directory_uri() . '/js/skip-link-focus-fix.js', array(), '20130115', true );
	
	wp_enqueue_style( 'impresa-google-arvo', '//fonts.googleapis.com/css?family=Arvo:400,400italic' );
	
    wp_enqueue_style( 'impresa-google-opensams', '//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,700italic,400,700,300' );
	
	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'impresa_scripts' );

function impresa_wp_head(){
	?>
	<!--[if lt IE 9]>
		<script src="<?php echo get_template_directory_uri(); ?>/js/modernizr.js" type="text/javascript"></script>
	<![endif]-->
	<?php
}
add_action('wp_head', 'impresa_wp_head');

/**
 * Implement the Custom Header feature.
 */
require get_template_directory() . '/inc/custom-header.php';

/**
 * Custom template tags for this theme.
 */
require get_template_directory() . '/inc/template-tags.php';

/**
 * Custom functions that act independently of the theme templates.
 */
require get_template_directory() . '/inc/extras.php';

/**
 * Customizer additions.
 */
require get_template_directory() . '/inc/customizer.php';

/**
 * Load Jetpack compatibility file.
 */
require get_template_directory() . '/inc/jetpack.php';

/* 
* Options panel
*/

define( 'OPTIONS_FRAMEWORK_DIRECTORY', get_template_directory_uri() . '/inc/' );
require_once dirname( __FILE__ ) . '/inc/options-framework.php';

/*
 * This is an example of how to add custom scripts to the options panel.
 * This one shows/hides the an option when a checkbox is clicked.
 *
 * You can delete it if you not using that option
 */

add_action( 'optionsframework_custom_scripts', 'optionsframework_custom_scripts' );

function optionsframework_custom_scripts() { ?>

<script type="text/javascript">
jQuery(document).ready(function() {

jQuery('#example_showhidden').click(function() {
  jQuery('#section-example_text_hidden').fadeToggle(400);
});

if (jQuery('#example_showhidden:checked').val() !== undefined) {
jQuery('#section-example_text_hidden').show();
}

});
</script>

<?php
}

/*
 * Options panel Customizer.
 */
if ( !function_exists( 'of_get_option' ) ) {
function of_get_option($name, $default = false) {
$optionsframework_settings = get_option('optionsframework');
// Gets the unique option id
$option_name = $optionsframework_settings['id'];
if ( get_option($option_name) ) {
$options = get_option($option_name);
}
if ( isset($options[$name]) ) {
return $options[$name];
} else {
return $default;
}
}
}

/*
 * Breadcrumb
 */ 
function ImpresaBreadcrumb() {
    echo '<div class="impresabreadcrumb">';
    if (!is_front_page()) {
        echo '<a href="'. esc_url(home_url('/')) .'">';
        echo 'Home';
        echo "</a> &#187; ";
        if (is_category() || is_single()) {
            the_category(' &#187; ');
            if (is_single()) {
                echo " &#187; ";
                the_title();
            }
        } elseif (is_page()) {
            echo the_title();
        }
    }
        echo '</div>';
}

/*
 * Add favicon.
 */
function impresa_favicon() { ?>
<?php if ( of_get_option('favicon_uploader')) { ?>
    <link rel="shortcut icon" href="<?php echo of_get_option( 'favicon_uploader', '' ); ?>" />
<?php } ?>
<?php if ( of_get_option('icon_iphone')) { ?>
    <link rel="apple-touch-icon" sizes="57x57" href="<?php echo of_get_option( 'icon_iphone', '' ); ?>">
<?php } ?>
<?php if ( of_get_option('icon_ipad')) { ?>
	<link rel="apple-touch-icon" sizes="76x76" href="<?php echo of_get_option( 'icon_ipad', '' ); ?>">
<?php } ?>
<?php if ( of_get_option('icon_iphone_retina')) { ?>
	<link rel="apple-touch-icon" sizes="120x120" href="<?php echo of_get_option( 'icon_iphone_retina', '' ); ?>">
<?php } ?>
<?php if ( of_get_option('icon_ipad_retina')) { ?>
	<link rel="apple-touch-icon" sizes="152x152" href="<?php echo of_get_option( 'icon_ipad_retina', '' ); ?>">
<?php } ?>
<?php if ( of_get_option('win_tile_image')) { ?>
    <meta name="msapplication-TileImage" content="<?php echo of_get_option( 'win_tile_image', '' ); ?>"/>
<?php } ?>
<?php if ( of_get_option('win_tile_color')) { ?>
	<meta name="msapplication-TileColor" content="<?php echo of_get_option( 'win_tile_color', '' ); ?>"/>
<?php } ?>
<?php }
add_action('wp_head', 'impresa_favicon');

/*
 * Custom xcerpt.
 */

// Changing excerpt length
function new_excerpt_length($length) {
return 100;
}
add_filter('excerpt_length', 'new_excerpt_length');

// Replaces the excerpt "more" text by a link
function new_excerpt_more($more) {
       global $post;
	return '...<br><a class="moretag" href="'. get_permalink($post->ID) . '">'. __('Read more &#8594;' ,'impresa') . '</a>';
}
add_filter('excerpt_more', 'new_excerpt_more');

/*
 * Schema.org.
 */
 
function html_tag_schema()
{
    $schema = 'http://schema.org/';

    // Is single post
    if(is_single())
    {
        $type = "Article";
    }
    // Is author page
    elseif( is_author() )
    {
        $type = 'ProfilePage';
    }
    // Is search results page
    elseif( is_search() )
    {
        $type = 'SearchResultsPage';
    }
    else
    {
        $type = 'WebPage';
    }

    echo 'itemscope="itemscope" itemtype="' . $schema . $type . '"';
}

/*
 * Woocommerce support.
 */
remove_action( 'woocommerce_before_main_content', 'woocommerce_output_content_wrapper', 10);
remove_action( 'woocommerce_after_main_content', 'woocommerce_output_content_wrapper_end', 10);
add_action('woocommerce_before_main_content', 'impresa_wrapper_start', 10);
add_action('woocommerce_after_main_content', 'impresa_wrapper_end', 10);

function impresa_wrapper_start() {
  echo '<section id="main" class="twelve columns">';
}

function impresa_wrapper_end() {
  echo '</section>';
}
add_theme_support( 'woocommerce' );