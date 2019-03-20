library(rmarkdown)
library(magrittr)
library(networkD3)


# Plot


links = read.table("links.txt")
nodes = read.table("nodes.txt")
weblinks <- c(read.table("hyperlinks.txt"))

ColourScale <- 'd3.scaleOrdinal()
            .domain(["1", "2", "3", "4"])
            .range(["#1722C1", "#90d185", "#138400", "#8e20c1"]);'

fn <- forceNetwork(Links = links, Nodes = nodes,
             Source = "source", Target = "target",
             Value = "value", NodeID = "name",
             Group = "group", opacity = 1.,
             colourScale = ColourScale, fontSize = 12)
fn$x$nodes$hyperlink <- weblinks
fn$x$options$clickAction = 'window.open(d.hyperlink)'

fn%>%
  saveNetwork(file = 'network.html')