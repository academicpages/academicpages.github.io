<?php
/**
 * The template used for displaying page content in page.php
 */
?>
<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
		<h1 class="entry-title" itemprop="name"><?php the_title(); ?></h1>
	</header><!-- .entry-header -->
	<div class="entry-content sitemap" itemprop="mainContentOfPage">

<div class="five columns">
<!-- Pages -->
	<h3><?php echo __('Pages', 'impresa'); ?></h3>  
    <ul><?php wp_list_pages("title_li=" ); ?></ul>
</div>

<div class="five columns">
<!-- Posts -->
    <h3><?php echo __('Posts', 'impresa'); ?></h3>  
    <ul><?php wp_get_archives('type=postbypost'); ?></ul>
</div>

<div class="five columns">
<!-- Authors -->
	<h3><?php echo __('Authors', 'impresa'); ?></h3>  
    <ul><?php wp_list_authors( 'optioncount=true'); ?></ul>    
    
<!-- Categories -->
	<h3><?php echo __('Categories', 'impresa'); ?></h3>  
    <ul><?php wp_list_categories('title_li='); ?></ul>  
</div>

</div><!-- .entry-content -->
	<?php edit_post_link( __( 'Edit', 'impresa' ), '<footer class="entry-meta"><span class="edit-link">', '</span></footer>' ); ?>
</article><!-- #post-## -->
