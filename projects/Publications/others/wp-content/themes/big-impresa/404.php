<?php
/**
 * The template for displaying 404 pages (Not Found).
 */

get_header(); ?>

	<div id="primary" class="content-area container">
		<main id="main" class="site-main" role="main">

			<section class="error-404 not-found">
				<header class="page-header">
					<h1 class="page-title"><?php _e( 'Oops! That page can&rsquo;t be found.', 'impresa' ); ?></h1>
				</header><!-- .page-header -->

				<div class="page-content">
                	<div class="message-404">
					<p><?php _e( 'It looks like nothing was found at this location. Maybe try one of the links below or a search?', 'impresa' ); ?></p>
					<?php get_search_form(); ?>
					</div><!-- .message-404 -->
					
                    <div class="widget widget_recent_posts six columns">
					<?php the_widget( 'WP_Widget_Recent_Posts' ); ?>
					</div><!-- .widget -->
                    
					<?php if ( impresa_categorized_blog() ) : // Only show the widget if site has multiple categories. ?>
					<div class="widget widget_categories six columns">
						<h2 class="widgettitle"><?php _e( 'Most Used Categories', 'impresa' ); ?></h2>
						<ul>
						<?php
							wp_list_categories( array(
								'orderby'    => 'count',
								'order'      => 'DESC',
								'show_count' => 1,
								'title_li'   => '',
								'number'     => 10,
							) );
						?>
						</ul>
					</div><!-- .widget -->
					
					<?php endif; ?>
					
                    <div class="widget widget_archives_tag four columns">
					<?php
					/* translators: %1$s: smiley */
					$archive_content = '<p>' . sprintf( __( 'Try looking in the monthly archives. %1$s', 'impresa' ), convert_smilies( ':)' ) ) . '</p>';
					the_widget( 'WP_Widget_Archives', 'dropdown=1', "after_title=</h2>$archive_content" );
					?>
                   
					<?php the_widget( 'WP_Widget_Tag_Cloud' ); ?>
                    </div><!-- .widget -->

				</div><!-- .page-content -->
			</section><!-- .error-404 -->

		</main><!-- #main -->
	</div><!-- #primary -->

<?php get_footer(); ?>