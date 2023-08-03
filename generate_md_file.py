# generate_md_file.py
import re
from Bio import Entrez, Medline
import pandas as pd

Entrez.email = "A.N.Other@example.com"
def get_pub(val, keyword):
    """
    This function retrieves the publication data from Pubmed database by searching the keyword.
    
    Parameters:
    val (int): The maximum number of results to return.
    keyword (str): The keyword to search for in the Pubmed database.
    
    Returns:
    tuple: Tuple of two dataframes - 'publication_data' and 'df'. 
    'publication_data' is the raw data retrieved from the Pubmed database, 
    and 'df' is the cleaned data with columns 'Published on', 'Title', 'Authors', 'PubchemID', 'DOI'.
    
    """
    # Search for the keyword in the Pubmed database and retrieve the maximum number of results specified by 'val'
    result = Entrez.read(Entrez.esearch(db="pubmed", retmax=int(val), term=keyword))
    ids = result["IdList"]
    
    # Batch process the retrieved results to avoid exceeding the API call limit
    batch_size = 100
    batches = [ids[x:x + 100] for x in range(0, len(ids), batch_size)]   
    record_list = []
    for batch in batches:
        handle = Entrez.efetch(db="pubmed", id=batch, rettype="medline", retmode="text")
        records = Medline.parse(handle)
        record_list.extend(list(records))
    
    # Load the data as a dataframe
    publication_data = pd.DataFrame(record_list)
    # Clean the data by removing rows with missing publication dates and adding a "Year" column
    publication_data.dropna(subset=["EDAT"], inplace=True)
    publication_data["Year"] = (publication_data["EDAT"].astype(str).str[0:4].astype(int))
    
    # Create a new dataframe with columns 'Published on', 'Title', 'Authors', 'PubchemID', 'DOI'
    dic = {'Published on': publication_data["DP"], 
        'Title': publication_data['TI'], 'Authors': publication_data["AU"],
        "DOI": publication_data["LID"], 'PubchemID': publication_data["PMID"],
        "Abstract":publication_data["AB"], 'Journal': publication_data["JT"],
        "PublishedDate":publication_data["DP"]
        }
    df = pd.DataFrame(dic)
    # Clean the 'DOI' column by removing '[doi]' and adding 'https://doi.org/' in front of each entry
    df['DOI'] = df['DOI'].str.replace(' \[doi\]', '')
    df['DOI'] = 'https://doi.org/' + df['DOI']
    
    return publication_data, df

def generate_md_file(author):
    publication_data, df = get_pub(10, author)  # Fetching the publication data using the 'get_pub' function
    for _, row in df.iterrows():
        title = row["Title"]
        authors = row["Authors"]
        published_on = row["Published on"]
        doi = row["DOI"]
        pubchem_id = row["PubchemID"]
        abstract = row["Abstract"]
        date = row["PublishedDate"]
        journal = row["Journal"]

        # Generate the permalink from Pubmed ID (PubchemID)
        permalink = f"PMID-{pubchem_id}"
        

        filename = f"_publications/{permalink}.md" 
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"title: \"{title}\"\n")
            f.write("collection: publications\n")
            f.write(f"permalink: /publication/{permalink}\n")
            f.write(f"date: {date}\n")
            f.write(f"venue: '{journal}'\n")
            f.write("pubtype: 'journal'\n")
            f.write(f"authors: '{', '.join(authors)}'\n")
            f.write("excerpt_separator: \"\"\n")
            f.write("---\n\n")
            f.write(f"### Abstract\n{abstract}\n\n")
            f.write(f"DOI : \n{doi}\n\n")  # Adding the DOI information to the .md file
            f.write(f"PubchemID : \n{pubchem_id}\n\n")  # Adding the PubchemID information to the .md file

if __name__ == "__main__":
    generate_md_file("Avratanu Biswas")
