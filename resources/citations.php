<style>
html, body, form, table, div, h1, h2, h3, h4, h5, h6, img, ol, ul, li, button {
    margin: 0px;
    padding: 0px;
    border: 0px none;
    color: #fff;
}

table {
    border-collapse: collapse;
    border-width: 0px;
    empty-cells: show;
}

body, td {
    font-size: 13px;
    font-family: Arial,sans-serif;
    line-height: 1.24;
}

.gsc_g_hist_wrp
{
	padding-top: 10px !important;
}

</style>

<?php  
	function filter_content($content, $url)
	{
		$contentText = '';
		$output = preg_match_all('/<div class="gsc_rsb_s gsc_prf_pnl" id="gsc_rsb_cit" role="region" aria-labelledby="gsc_prf_t-cit">(.*)<\/div><div class="gsc_rsb_s gsc_prf_pnl" id="gsc_rsb_co" role="region" aria-labelledby="gsc_prf_t-ath">/is',$content,$matches);
		// if this has not worked try another variant:
		if(!isset($matches[1][0]))
		{
		$output = preg_match_all('/<div class="gsc_rsb_s gsc_prf_pnl" id="gsc_rsb_cit" role="region" aria-labelledby="gsc_prf_t-cit">(.*)<\/div><div class="gsc_lcl" role="main" id="gsc_prf_w">/is',$content,$matches);
		}

		$contentText = isset($matches[1][0])?$matches[1][0]:'e1';

		preg_match_all('/Citations<\/a><\/td><td class="gsc_rsb_std">(\d+)<\/td>/is',$contentText,$matches);
		$citations = isset($matches[1][0])?$matches[1][0]:'e2';

		preg_match_all('/h-index<\/a><\/td><td class="gsc_rsb_std">(\d+)<\/td>/is',$contentText,$matches);
		$hindex = isset($matches[1][0])?$matches[1][0]:'e3';

		preg_match_all('/<style>(.+)/is',$contentText,$matches);
		$contentText2 = isset($matches[1][0])?$matches[1][0]:'e4';
 
		$contentText2 = '<style>'.$contentText2;

		$dom = new DOMDocument();
		$dom->preserveWhiteSpace = FALSE;
		$dom->loadHTML($contentText2);
		$dom->formatOutput = TRUE;

		$links = $dom->getElementsByTagName('a');

		//Loop through each <a> tags and replace them by their text content    
		for ($i = $links->length - 1; $i >= 0; $i--)
		{
			$linkNode = $links->item($i);
			$text = $linkNode->textContent;
			$style = $linkNode->getAttribute("style");
			$class = $linkNode->getAttribute("class");
			$div = $dom->createElement("div", $text);
			$div->setAttribute("class","$class");
			$div->setAttribute("style","$style");
			$linkNode->parentNode->replaceChild($div, $linkNode);
		}

		$contentText2 = $dom->saveHTML();
		$contentText2 = 'Citations according to <a href="'.$url.'">Google Scholar</a>: '
                                .$citations.' (h-index: '.$hindex.')'.$contentText2;
		
		return $contentText2; 
	}

	if($_GET["id"] != "" && $_GET["lang"] != "")
	{
		$curl = curl_init();

		$id = htmlspecialchars($_GET['id'], ENT_QUOTES, 'UTF-8');
		$lang = htmlspecialchars($_GET['lang'], ENT_QUOTES, 'UTF-8');
		$url = "http://scholar.google.de/citations?user=".$id."&hl=".$lang;

		curl_setopt($curl, CURLOPT_URL, $url);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
		curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 60);

		print filter_content( curl_exec($curl), $url );
		#print curl_exec($curl);
	}
	else
	{
		print "ERROR: Cannot find Google Scholar Account </br>";
	}
?>
