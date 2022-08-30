# load packages
if (!require("pacman")) install.packages("pacman"); library(pacman) 
p_load(scholar,ggplot2,scales)

# 
cit <- get_citation_history('3FHDoL0AAAAJ&hl')
#png('scholar_citations.png',width=800,height=300,res=150)
p = ggplot(cit,aes(x=year,y=cites))+
  geom_bar(stat='identity')+
  theme_bw()+
  xlab('Year')+
  ylab('Cites') +
  scale_y_continuous(labels = number_format(accuracy = 1), breaks = round(seq(min(cit$cites), max(cit$cites), by = 1),1)) +
  scale_x_continuous(breaks = round(seq(min(cit$year), max(cit$year), by = 1),1)) +
  annotate('text',label=format(Sys.time(), "%Y-%m-%d"),x=-Inf,y=Inf,vjust=1.5,hjust=-0.05,size=3,colour='gray')  + 
  theme_classic() +
  theme(#axis.text.y   = element_text(size=14),
        #axis.text.x   = element_text(size=14),
        #axis.title.y  = element_text(size=14),
        #axis.title.x  = element_text(size=14),
        #panel.background = element_blank(),
        #panel.grid.major = element_blank(), 
        #panel.grid.minor = element_blank(),
        #axis.line = element_line(colour = "black"),
        panel.border = element_rect(colour = "black", fill=NA, size=1)
  ) +
  ggtitle("Google Scholar Cites")
  
# p

ggsave(
  "google_citations.pdf",
  plot = last_plot(),
  path = "/Users/hectorbahamonde/Dropbox/",
  scale = 1,
  device = "pdf",
  width = 800,
  height = 300,
  units = c("px"),
  dpi = 100
)

dev.off()
