<?php
/**
 * The Template for displaying all single posts.
 */

get_header(); ?>

	<?php if ( of_get_option('sidebar-post') == '2c-l-fixed twelve columns' ) {
  		get_sidebar();
	}?>
    
	<div id="primary" class="content-area <?php echo of_get_option( 'sidebar-post' ); ?>">
		<main id="main" class="site-main" role="main">
	<?php ImpresaBreadcrumb(); ?>
		<?php while ( have_posts() ) : the_post(); ?>
			<?php get_template_part( 'content/content', 'single' ); ?>
			<?php impresa_post_nav(); ?>
			<?php
				// If comments are open or we have at least one comment, load up the comment template
				if ( comments_open() || '0' != get_comments_number() ) :
					comments_template();
				endif;
			?>
		<?php endwhile; // end of the loop. ?>
		</main><!-- #main -->
	</div><!-- #primary -->
	
	<?php if ( of_get_option('sidebar-post') == '2c-r-fixed twelve columns' ) {
  		get_sidebar();
	}?>
    
<?php get_footer(); ?>