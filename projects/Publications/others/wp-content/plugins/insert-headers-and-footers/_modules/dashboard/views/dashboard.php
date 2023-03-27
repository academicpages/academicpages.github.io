<?php
/**
* Dashboard RSS Feed Widget
*/
?>
<div class="rss-widget">
	<img src="http://cdn.wpbeginner.com/pluginimages/wpbeginner.gif" class="alignright" />
	
	<ul>
		<?php
		foreach ($rssPosts->item as $key=>$rssPost) {
			?>
			<li>
				<a href="<?php echo (string) $rssPost->link; ?>" target="_blank" class="rsswidget"><?php echo (string) $rssPost->title; ?></a>
				<span class="rss-date"><?php echo date('F j, Y', strtotime($rssPost->pubDate)); ?></span>
			</li>
			<?php	
		}
		?>
		
		<li>
			<hr />
			<a href="http://feeds2.feedburner.com/wpbeginner" class="rss" target="_blank"><?php _e('Subscribe with RSS', $this->dashboard->name); ?></a>
			<a href="http://www.wpbeginner.com/wordpress-newsletter/" class="email" target="_blank"><?php _e('Subscribe by email', $this->dashboard->name); ?></a>
			<a href="http://facebook.com/wpbeginner/" class="facebook" target="_blank"><?php _e('Join us on Facebook', $this->dashboard->name); ?></a>
		</li>
	</ul>
</div>
