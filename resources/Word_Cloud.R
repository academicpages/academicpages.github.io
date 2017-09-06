cat("\014")
rm(list=ls())

# source: https://www.r-bloggers.com/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know/

############################
#### Loadings
############################

# Load the earthquake data
if (!require("pacman")) install.packages("pacman"); library(pacman)
p_load(tm, SnowballC, wordcloud, RColorBrewer)



##

# Pandoc papers


#  Sectoral Origins of Income Taxation: Industrial Development and The Case of Chile (1900-2010)
system("pandoc --highlight-style=espresso --filter=pandoc-citeproc --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/library.bib --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/Bahamonde_BibTex2013.bib --csl=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/APA_Style.csl -s /Users/hectorbahamonde/RU/Dissertation/Papers/IncomeTaxAdoption/Bahamonde_IncomeTaxAdoption.tex -o /Users/hectorbahamonde/RU/Dissertation/Papers/IncomeTaxAdoption/Bahamonde_IncomeTaxAdoption.txt")



#  Structural Transformations and State Institutions in Latin America, 1900-2010
system("pandoc --highlight-style=espresso --filter=pandoc-citeproc --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/library.bib --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/Bahamonde_BibTex2013.bib --csl=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/APA_Style.csl -s /Users/hectorbahamonde/RU/Dissertation/Papers/NegativeLink/Bahamonde_NegativeLink.tex -o /Users/hectorbahamonde/RU/Dissertation/Papers/NegativeLink/Bahamonde_NegativeLink.txt")


#  Clientelism Brazil Paper
system("pandoc --highlight-style=espresso --filter=pandoc-citeproc --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/library.bib --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/Bahamonde_BibTex2013.bib --csl=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/APA_Style.csl -s /Users/hectorbahamonde/RU/research/Clientelism_paper/Bahamonde_Clientelism_Paper.tex -o /Users/hectorbahamonde/RU/research/Clientelism_paper/Bahamonde_Clientelism_Paper.txt")



# Earthquake Paper
system("pandoc --highlight-style=espresso --filter=pandoc-citeproc --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/library.bib --biblio=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/Bahamonde_BibTex2013.bib --csl=/Users/hectorbahamonde/RU/Bibliografia_PoliSci/APA_Style.csl -s /Users/hectorbahamonde/RU/Dissertation/Papers/Earthquake_Paper/Bahamonde_Earthquake_Paper.tex -o /Users/hectorbahamonde/RU/Dissertation/Papers/Earthquake_Paper/Bahamonde_Earthquake_Paper.txt")



## import text
text1 <- readLines("/Users/hectorbahamonde/RU/Dissertation/Papers/IncomeTaxAdoption/Bahamonde_IncomeTaxAdoption.txt")

text2 <- readLines("/Users/hectorbahamonde/RU/Dissertation/Papers/NegativeLink/Bahamonde_NegativeLink.txt")

text3 <- readLines("/Users/hectorbahamonde/RU/research/Clientelism_paper/Bahamonde_Clientelism_Paper.txt")

text4 <- readLines("/Users/hectorbahamonde/RU/Dissertation/Papers/Earthquake_Paper/Bahamonde_Earthquake_Paper.txt")





alltext = as.vector(c(text1,text2,text3))


# Load the data as a corpus
docs <- Corpus(VectorSource(alltext))

# inspect(docs)

toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")
docs <- tm_map(docs, toSpace, "\\[")
docs <- tm_map(docs, toSpace, "\\]")
docs <- tm_map(docs, toSpace, "\\^")


text3 <- readLines("/Users/hectorbahamonde/RU/research/Clientelism_paper/Bahamonde_Clientelism_Paper.txt")


# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))
# Remove numbers
docs <- tm_map(docs, removeNumbers)
# Remove english common stopwords
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removeWords, c("paper", "explain", "see", "also", "one", "two", "different", "span", "example", "however", "important", "hence", "argue", "since", "https", "well")) 
# Remove punctuations
docs <- tm_map(docs, removePunctuation)
# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)
# Text stemming
# docs <- tm_map(docs, stemDocument)

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)


#
dev.new(width=3, height=3)
set.seed(604)

png(filename="/Users/hectorbahamonde/RU/Web/hbahamonde.github.io/resources/wordcloud.png", width = 336, height = 280, res = 72)

wordcloud(words = d$word, freq = d$freq, min.freq = 10,
          max.words=200, rangesizefont = c(5, 20), random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
dev.off()
