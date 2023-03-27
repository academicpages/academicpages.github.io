<?php
/**
 * Social link.
 */
?>

<div class="social-url">
        <?php if ( of_get_option('facebook_url') ) {
              $facebook_url = of_get_option('facebook_url', '');
			  echo "<a href='$facebook_url' title='Facebook' target='_blank' class='facebook-icon'><span class='social_facebook'></span></a>";
		}?>
         <?php if ( of_get_option('twitter_url') ) {
              $twitter_url = of_get_option('twitter_url', '');
			  echo "<a href='$twitter_url' title='Twitter' target='_blank' class='twitter-icon'><span class='social_twitter'></span></a>";
		}?>
         <?php if ( of_get_option('google_url') ) {
              $google_url = of_get_option('google_url', '');
			  echo "<a href='$google_url' title='Google Plus' target='_blank' class='google-icon'><span class='social_googleplus'></span></a>";
		}?>
        <?php if ( of_get_option('pinterest_url') ) {
              $pinterest_url = of_get_option('pinterest_url', '');
			  echo "<a href='$pinterest_url' title='Pinterest' target='_blank' class='pinterest-icon'><span class='social_pinterest'></span></a>";
		}?>
        <?php if ( of_get_option('tumblr_url') ) {
              $tumblr_url = of_get_option('tumblr_url', '');
			  echo "<a href='$tumblr_url' title='Tumblr' target='_blank' class='tumblr-icon'><span class='social_tumblr'></span></a>";
		}?>
        <?php if ( of_get_option('instagram_url') ) {
              $instagram_url = of_get_option('instagram_url', '');
			  echo "<a href='$instagram_url' title='Instagram' target='_blank' class='instagram-icon'><span class='social_instagram'></span></a>";
		}?>
        
        <?php if ( of_get_option('linkedin_url') ) {
              $linkedin_url = of_get_option('linkedin_url', '');
			  echo "<a href='$linkedin_url' title='Linkedin' target='_blank' class='linkedin-icon'><span class='social_linkedin'></span></a>";
		}?>
        
        <?php if ( of_get_option('dribbble_url') ) {
              $dribbble_url = of_get_option('dribbble_url', '');
			  echo "<a href='$dribbble_url' title='Dribble' target='_blank' class='dribble-icon'><span class='social_dribbble'></span></a>";
		}?>
         <?php if ( of_get_option('vimeo_url') ) {
              $vimeo_url = of_get_option('vimeo_url', '');
			  echo "<a href='$vimeo_url' title='Vimeo' target='_blank' class='vimeo-icon'><span class='social_vimeo'></span></a>";
		}?>
        
        <?php if ( of_get_option('youtube_url') ) {
              $youtube_url = of_get_option('youtube_url', '');
			  echo "<a href='$youtube_url' title='Youtube' target='_blank' class='youtube-icon'><span class='social_youtube'></span></a>";
		}?>
        <?php if ( of_get_option('rss_url') ) {
              $rss_url = of_get_option('rss_url', '');
			  echo "<a href='$rss_url' title='RSS' target='_blank' class='rss-icon'><span class='social_rss'></span></a>";
		}?>
 </div><!-- .social url -->  