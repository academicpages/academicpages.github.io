<?php
/**
 * The template for displaying Search Results pages.
 */

get_header(); ?>

<section id="primary" class="content-area <?php echo of_get_option( 'sidebar-blog' ); ?>">
	<main id="main" class="site-main" role="main">

		<?php if ( have_posts() ) : ?>

			<header class="page-header">
				<h1 class="page-title"><?php printf( __( 'Search Results for: %s', 'impresa' ), '<span>' . get_search_query() . '</span>' ); ?></h1>
			</header><!-- .page-header -->

		<?php /* Start the Loop */ ?>
        
		<?php while ( have_posts() ) : the_post(); ?>
			<?php get_template_part( 'content/content', 'search' ); ?>

		<?php endwhile; ?>
			<?php impresa_paging_nav(); ?>

		<?php else : ?>
			<?php get_template_part( 'content/content', 'none' ); ?>

		<?php endif; ?>

	</main><!-- #main -->
</section><!-- #primary -->

<?php get_footer(); ?>
