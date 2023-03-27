<?php
/**
 * The content
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

   	<header class="entry-header">
		<h1 class="entry-title">
	<?php the_title(); ?>
        <?php /* <a href="<?php the_permalink(); ?>" rel="bookmark"><?php the_title(); ?></a> */ ?>
        </h1>
	<?php if ( 'post' == get_post_type() ) : ?><!--
		<div class="entry-meta">
			<?php impresa_posted_on(); ?>
		</div>--> <!-- .entry-meta -->
		<?php endif; ?>
    </header><!-- .entry-header -->

	<?php if ( is_search() ) : // Only display Excerpts for Search ?>
		<div class="entry-summary">
			<?php the_content(); ?>
		</div><!-- .entry-summary -->
	
	<?php else : ?>
    
	<div class="entry-content">
    	<?php if ( of_get_option('featured_image_blog') == 'yes' ) if ( has_post_thumbnail()) : ?>
       		<a href="<?php the_permalink(); ?>" title="<?php the_title_attribute(); ?>" >
   		<?php the_post_thumbnail(); ?>
   			</a>
            
 	<?php endif; ?>
 
	<?php the_content( __( 'Continue reading <span class="meta-nav">&rarr;</span>', 'impresa' ) ); ?>
		<?php
			wp_link_pages( array(
				'before' => '<div class="page-links">' . __( 'Pages:', 'impresa' ),
				'after'  => '</div>',
			) );
		?>
	</div><!-- .entry-content -->
    
	<?php endif; ?>

	<footer class="entry-meta">
	
		<?php if ( ! post_password_required() && ( comments_open() || '0' != get_comments_number() ) ) : ?>
		<span class="comments-link"><?php comments_popup_link( __( 'Leave a comment', 'impresa' ), __( '1 Comment', 'impresa' ), __( '% Comments', 'impresa' ) ); ?></span>
		<?php endif; ?>

		<?php edit_post_link( __( 'Edit', 'impresa' ), '<span class="edit-link">', '</span>' ); ?>
	</footer><!-- .entry-meta -->
    
</article><!-- #post-## -->