<?php
/**
 * The template used for displaying page content in page-notitle.php
 */
?>
<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
	</header><!-- .entry-header -->
	<div class="entry-content">
		<?php the_content(); ?>
		<?php
			wp_link_pages( array(
				'before' => '<div class="page-links">' . __( 'Pages:', 'impresa' ),
				'after'  => '</div>',
			) );?>
	</div><!-- .entry-content -->
	<?php edit_post_link( __( 'Edit', 'impresa' ), '<footer class="entry-meta"><span class="edit-link">', '</span></footer>' ); ?>
</article><!-- #post-## -->