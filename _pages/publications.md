---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Full publication list can be found here: [ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586&sort=date%20desc%2C%20bibcode%20desc&p_=0) and here: [arXiv](https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header)

<div id="publications-api"></div>
<div id="publications-fallback">
  {% include publications-list.html %}
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
  const token = "D3EEeNji8fD6lSeZa2yLhvnWtqEP0RhDSlJTpsBs";
  const orcid = "0000-0002-5992-7586";
  const query = `orcid:${orcid}`;
  
  // Try to load publications from the ADS API
  $.ajax({
    url: "https://api.adsabs.harvard.edu/v1/search/query",
    type: "GET",
    dataType: "json",
    contentType: "application/json",
    headers: {
      "Authorization": `Bearer ${token}`
    },
    data: {
      q: query,
      fl: "title,author,year,bibcode,pub,volume,page",
      rows: 100,
      sort: "date desc"
    },
    success: function(data) {
      const publications = data.response.docs;
      if (publications && publications.length > 0) {
        let html = "<div class='publications-list'>";
        
        for (let i = 0; i < publications.length; i++) {
          const pub = publications[i];
          let authors = pub.author ? pub.author.join(", ") : "";
          
          // Truncate author list if too long
          if (authors.length > 100) {
            const authorArray = pub.author;
            if (authorArray.length > 5) {
              authors = `${authorArray.slice(0, 3).join(", ")}, et al.`;
            }
          }
          
          const year = pub.year || "";
          const title = pub.title ? pub.title[0] : "";
          const journal = pub.pub || "";
          const volume = pub.volume || "";
          const page = pub.page ? pub.page[0] : "";
          const bibcode = pub.bibcode;
          const adsLink = `https://ui.adsabs.harvard.edu/abs/${bibcode}/abstract`;
          
          let journalInfo = "";
          if (journal) {
            journalInfo += journal;
            if (volume) journalInfo += `, ${volume}`;
            if (page) journalInfo += `, ${page}`;
          }
          
          html += `
            <div class="publication-item">
              <div class="publication-title"><a href="${adsLink}" target="_blank">${title}</a></div>
              <div class="publication-authors">${authors}</div>
              <div class="publication-journal">${journalInfo} (${year})</div>
            </div>
          `;
        }
        
        html += "</div>";
        
        // Show API results and hide fallback
        $("#publications-api").html(html);
        $("#publications-fallback").hide();
      } else {
        // If no publications were found, show fallback
        $("#publications-fallback").show();
        $("#publications-api").hide();
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
      // If there's an error, show fallback
      console.error("Error fetching publications:", textStatus, errorThrown);
      $("#publications-fallback").show();
      $("#publications-api").hide();
    }
  });
});
</script>
