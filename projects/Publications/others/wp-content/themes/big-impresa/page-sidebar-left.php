<?php
/**
  * Template Name: Page Sidebar Left
 */

get_header(); ?>

<?php get_sidebar(); ?>
	<div id="primary" class="content-area twelve columns">
		<main id="main" class="site-main" role="main">

			<?php while ( have_posts() ) : the_post(); ?>
				<?php get_template_part( 'content/content', 'page' ); ?>
            
				<?php
				// If comments are open or we have at least one comment, load up the comment template
				if ( comments_open() || '0' != get_comments_number() ) :
					comments_template();
				endif;?>
                
			<?php endwhile; // end of the loop. ?>

		</main><!-- #main -->
	</div><!-- #primary -->
<?php get_footer(); ?>