#!/bin/bash

#By Leonardo Pacciani-Mori, 11th July 2018
#This script gets the necessary information from the _publications folder and generates the data needed to create the network with the R script network.R
#It may be not written in the most intelligent or efficient way.
#In order to update the network, execute this script any time some changes are made in the _publications folder.

TEMP_AUTH="temp_auth.txt"		#definition of the files that will be used
TEMP_LINE="temp_line.txt"
TEMP_MISC="temp_misc.txt"
TEMP="temp.txt"
OUTPUT_AUTH="out_auth.txt"
OUTPUT_TITLE="out_title.txt"
OUTPUT_URL="out_URL.txt"
OUTPUT_TYPE="out_type.txt"
NODES="nodes.txt"
URL="hyperlinks.txt"
LINKS="links.txt"


echo "" > $URL
echo "" > $TEMP_AUTH		#creates blank temporary file
echo "" > $OUTPUT_TITLE
echo "" > $OUTPUT_URL
echo "" > $OUTPUT_TYPE
echo "" > $TEMP_MISC
echo "" > $TEMP_LINE
echo "" > $TEMP


#look for every file in _publications/, and extracts useful information and puts it into files needed to generate the network
for filename in ../_publications/*
do
	echo $(grep -h "authors" $filename | cut -d \' -f 2) >> $TEMP_AUTH	#extracts the author names from the file
	echo $(grep -h "title" $filename | cut -d \" -f 2) >> $OUTPUT_TITLE	#extracts the title of the article names from the file
	echo $(grep -h "paperurl" $filename | cut -d \' -f 2) >> $OUTPUT_URL	#extracts the url of the article from the file
	echo $(grep -h "excerpt" $filename | cut -d \: -f 2) >> $OUTPUT_TYPE	#extracts the type of the publication
done



sed -i '/^$/d' $TEMP_AUTH				#deletes first blank line
sed -i '/^$/d' $OUTPUT_TITLE
sed -i '/^$/d' $OUTPUT_URL
sed -i '/^$/d' $OUTPUT_TYPE
cat $TEMP_AUTH | sed "s/,\ /\n/g" | perl -ne 'print unless $seen{$_}++' > $OUTPUT_AUTH	#deletes duplicate lines and returns a newline separated list of all the authors


sed -i '/Leonardo Pacciani/d' $OUTPUT_AUTH	#removes "Leonardo Pacciani" from the author list


authN=$(cat $OUTPUT_AUTH | wc -l)		#total number of authors
titleN=$(cat $OUTPUT_TITLE | wc -l)		#total number of articles


echo " 	name	group" > $NODES		#creates file with nodes data
echo "	source	target	value" > $LINKS	#creates file with link data


for i in $(seq 1 $authN)	#loops over all authors and add the relative line in $NODES and $URL
do
	echo -e "$((i-1))\t\""$(sed "${i}q;d" $OUTPUT_AUTH)"\"\t1" >> $NODES								#adds to $NODES the line relative to each author
	echo -e "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="$(sed "${i}q;d" $OUTPUT_AUTH | sed "s/\ /+/g") >> $URL	#adds to $URL the author's weblink (google scholar)
done	
#sed -i '/^$/d' $URL	#deletes first blank line


for i in $(seq 1 $titleN)	#loops over all articles and add the relative line in $NODES
do
	pubtype=$(sed "${i}q;d" $OUTPUT_TYPE)
	if (echo $pubtype | grep -qi "thesis"); then
	group=4
	elif (echo $pubtype | grep -qi "preprint"); then
	group=2
	else group=3
	fi
	echo -e "$((authN+i-1))\t\""$(sed "${i}q;d" $OUTPUT_TITLE)"\"\t${group}" >> $NODES	#adds to $NODES the line relative to each article
	echo -e $(sed "${i}q;d" $OUTPUT_URL) >> $URL					#adds to $URL the article's weblink
done

echo $(tr '\n' '\t' < $URL) > $URL	#substitutes newlines with horizontal tags in $URL



#now we have to make the links between the nodes

for i in $(seq 1 $authN)
do
	name=$(sed "${i}q;d" $OUTPUT_AUTH)
	grep "$name" $NODES >> $TEMP_LINE
done

	cat $TEMP_LINE | perl -ne 'print unless $seen{$_}++' > $TEMP_MISC	#deletes duplicate lines
	length=$(cat $TEMP_MISC | wc -l)
	for j in $(seq 2 $length)
	do
		source=$(sed "${j}q;d" $TEMP_MISC | cut -f 1)
		name=$(cat $TEMP_MISC | sed "${j}q;d" | grep -oP '(?<=").*(?=")')
		grep -n "$name" $TEMP_AUTH > $TEMP
		pubN=$(cat $TEMP | wc -l)		#number of publications in which the author appears

		for q in $(seq 1 $pubN)
		do
			targetline=$(sed "${q}q;d" $TEMP |cut -d ":" -f 1)
			target=$((targetline+authN-1))
			echo -e "$j\t${source}\t${target}\t1" >> $LINKS
			
		done
	
	done




cat $LINKS | sed "s/,\ /\n/g" | perl -ne 'print unless $seen{$_}++' > $TEMP_MISC	#deletes duplicate lines
cat $TEMP_MISC > $LINKS



echo "" > $TEMP_MISC
length=$(cat $LINKS | wc -l)
for ((k=2;k<=$length;k++))
do
oldline=$(sed "${k}q;d" $LINKS)
old_cut=$(cut -f 2-4 <<< $oldline)
newline=$(echo $((k-2))"\t"$old_cut)
sed -i "s/${oldline}/${newline}/" $LINKS
done




rm $TEMP_AUTH	#deletes auxiliary files
rm $OUTPUT_AUTH
rm $OUTPUT_TITLE
rm $OUTPUT_URL
rm $OUTPUT_TYPE
rm $TEMP_LINE
rm $TEMP_MISC
rm $TEMP

Rscript network.R

rm $URL
rm $NODES
rm $LINKS

#sed -i "s/http:/https:/g" network.html
