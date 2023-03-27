MY_NAME = "Bahador Saket";

// DISPLAY OPTIONS -------
SHOW_THUMBNAILS = true;
SHOW_TYPE_TAGS = true;
SHOW_YEAR_HEADINGS = true;
// Note that this is still organized by year,
// so it doesn't make sense for this to be true
// and SHOW_YEAR_HEADINGS to be false.
SHOW_TYPE_HEADINGS = false;
// If true, assumes that there is a pub_grouping mapping in the json object
USE_CUSTOM_GROUPS = false;
//-------------------------

// The order the that types are grouped during each year
GROUP_ORDER = ['dissertation', 'journal', 'conference', 'chapter', 'late-breaking work', 'workshop', 'poster', 'article', 'tech report', 'demo'];
// If using custom grouping, I use this order
// GROUP_ORDER = ['journal/chapter','conference/workshop', 'other'];

ICON_PATH =  "thumbnails/";
ICON_SIZE = 100;

// Assumes that we are only going to have 10
var tagColor;
// If we use customs group, this maps orig type name to custom group name
var groupMap;

d3.json('pubs.json', function(json){

    if (USE_CUSTOM_GROUPS)
      groupMap = d3.map(json.pub_grouping);

    createTypeColors(json.publications);

    var nested_data = d3.nest()
      .key(function(d) {return d.year;})
        .sortKeys(d3.descending)
      .key(function(d) { return USE_CUSTOM_GROUPS ? groupMap.get(d.type) : d.type; })
        .sortKeys(function(a,b) { return GROUP_ORDER.indexOf(a) - GROUP_ORDER.indexOf(b); })
      .entries(json.publications);

    buildYears(nested_data, '#publications');
});

function createTypeColors(d) {
  var types = [];
  d.forEach(function(pub) {
    if (types.indexOf(pub.type) < 0) {
      types.push(pub.type);
    }
  });
  tagColor = d3.scale.category10().domain(types);
}

// Organize by year of publication
function buildYears(pubData, target) {
  var years = d3.select(target).selectAll('.yearGroup')
    .data(pubData)
    .enter().append('div')
    .classed('yearGroup', true);

  if (SHOW_YEAR_HEADINGS)
    years.append('h3').text(function(d) {return d.key; });

  years.each(buildTypes);
}

// Organize by type of publication
function buildTypes() {
  var types = d3.select(this).selectAll('.typeGroup')
    .data(function(d) {return d.values; })
    .enter().append('div')
    .classed('typeGroup', true);

  if (SHOW_TYPE_HEADINGS)
    types.append('h3').text(function(d) { return d.key; });
  types.each(renderPubs);
}

// Generate publications
function renderPubs(pubData, target) {
  var pubs = d3.select(this).selectAll('pub')
      .data(function(d) {return d.values;});

  pubs.enter().append('div')
      .classed('pub', true);

  if (SHOW_THUMBNAILS) {
    // representative image
    var pubIcon = pubs.append('img')
      .classed('thumbnail', true)
      .attr('src', function(d) {
        return ICON_PATH + d.thumbnail;
      });
  }


// Div for all the publication info
  var pubInfo = pubs.append('div')
    .classed('pubInfo', true)
    // .style('height',ICON_SIZE);

    
  if (SHOW_TYPE_TAGS) {
    // tag that shows pub type
    pubInfo.append('text')
      .classed('type-tag', true)
      .text(function(d) { return d.type + ''; })
      .style('background-color', function(d) {
        return tagColor(d.type);
      })
      .style('opacity', 0.5);
  }

  // title
  var titles = pubInfo.append('div')
      .classed('title', true)
      .append('a')
      .attr('href', function(d) { return d.pdf; })
      .text(function(d) { return d.title; });

  // Add award icon and text


  //authors
  pubInfo.append('div')
      .classed('authors', true)
      .html(function(d) {
        return d.author.join(", ")
                       .replace(MY_NAME, '<span class="me">' + MY_NAME + '</span>');
      });

  // venue, year
  pubInfo.append('div')
      .classed('venue', true)
      .text(function(d) { return d.venue + ' '+ d.year; });



  var awardIcon = pubInfo.selectAll('.authors')
      .filter(function(d) { return d.award || ''});

  // awardIcon.append('img')
  //     .classed('award-icon', true)
  //     .attr('src', 'icons/cert.png')
  //     .attr('width', 13);

  awardIcon.append('div')
    .classed('award-text', true)
    .text(function(d) { return d.award; });


  // add supplemental links
  pubInfo.append('text')
    .classed('supp', true)
    .html(function(d) {
      // First add paper pdf (if there is one)
      var supplementals = ''
      if (d.hasOwnProperty('pdf'))
        supplementals += '<a href="' + d.pdf + '"> pdf </a>';
      else
        supplementals += ''

      // then add everything else
      for (var link in d.supp) {
        supplementals += '| <a href="' + d.supp[link] + '"> ' + link + '</a> ';
      }
      return supplementals;
    });
}