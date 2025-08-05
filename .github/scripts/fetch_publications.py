#!/usr/bin/env python3
"""
Script to fetch publications from the NASA ADS API and save them as JSON.
This script is intended to be run via GitHub Actions.
"""

import os
import json
import requests
from datetime import datetime
import sys
import traceback

# Configuration
ORCID = "0000-0002-5992-7586"
OUTPUT_FILE = "assets/js/publications.json"
ADS_API_URL = "https://api.adsabs.harvard.edu/v1/search/query"
DEBUG = True  # Set to True for more detailed logging

def debug_log(message):
    """Print debug messages if DEBUG is enabled."""
    if DEBUG:
        print(f"DEBUG: {message}")

def calculate_summary_stats(publications):
    """Calculate comprehensive publication statistics."""
    if not publications:
        return {
            'total_papers': 0,
            'total_citations': 0,
            'h_index': 0,
            'i10_index': 0,
            'first_author_papers': 0,
            'avg_citations_per_paper': 0.0,
            'last_updated': datetime.now().strftime("%Y-%m-%d")
        }
    
    total_papers = len(publications)
    total_citations = sum(pub.get('citation_count', 0) for pub in publications)
    
    # H-index calculation
    citations = sorted([pub.get('citation_count', 0) for pub in publications], reverse=True)
    h_index = 0
    for i, citation_count in enumerate(citations):
        if citation_count >= i + 1:
            h_index = i + 1
        else:
            break
    
    # i10-index (papers with 10+ citations)
    i10_index = sum(1 for pub in publications if pub.get('citation_count', 0) >= 10)
    
    # First author papers - check if Yuan, Sihan appears first
    # The author field format from ADS is "LastName, FirstName, ..."
    first_author_papers = 0
    for pub in publications:
        authors = pub.get('authors', '')
        if authors:
            # Check if the first author is Yuan, S. or Yuan, Sihan
            first_author = authors.split(',')[0:2]  # Get first two parts
            if len(first_author) >= 2:
                if first_author[0].strip().lower() == 'yuan' and \
                   (first_author[1].strip().lower().startswith('s') or 
                    first_author[1].strip().lower().startswith('sihan')):
                    first_author_papers += 1
                    # Add a flag to the publication for frontend filtering
                    pub['is_first_author'] = True
                else:
                    pub['is_first_author'] = False
    
    avg_citations = round(total_citations / total_papers, 1) if total_papers > 0 else 0.0
    
    return {
        'total_papers': total_papers,
        'total_citations': total_citations,
        'h_index': h_index,
        'i10_index': i10_index,
        'first_author_papers': first_author_papers,
        'avg_citations_per_paper': avg_citations,
        'last_updated': datetime.now().strftime("%Y-%m-%d")
    }

def main():
    try:
        # Get the ADS token from environment variables
        ads_token = os.environ.get("ADS_TOKEN")
        if not ads_token:
            print("Error: ADS_TOKEN environment variable not set")
            print("Please add your ADS token as a GitHub secret named ADS_TOKEN")
            exit(1)
        
        debug_log(f"Token found, length: {len(ads_token)}")
        debug_log(f"Token starts with: {ads_token[:4]}...")
        
        # Prepare the API request
        headers = {
            "Authorization": f"Bearer {ads_token}",
            "Content-Type": "application/json"
        }
        
        params = {
            "q": f"orcid:{ORCID}",
            "fl": "title,author,year,bibcode,pub,volume,page,doi,arxiv_class,identifier,citation_count,read_count",
            "rows": 200,
            "sort": "date desc"
        }
        
        # Make the API request
        print(f"Fetching publications for ORCID: {ORCID}")
        
        # Try with a timeout to avoid hanging
        try:
            debug_log("Sending API request to ADS...")
            response = requests.get(ADS_API_URL, headers=headers, params=params, timeout=30)
            debug_log(f"Response status code: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Error: API request failed with status code {response.status_code}")
                print(f"Response text: {response.text[:500]}...")  # Print first 500 chars of response
                
                # Create a minimal output file with error information
                create_error_output("API request failed", response.status_code, response.text[:500])
                exit(1)
            
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            create_error_output("Request exception", str(e), traceback.format_exc())
            exit(1)
        
        # Parse the response
        try:
            data = response.json()
            debug_log("API response parsed as JSON successfully")
        except json.JSONDecodeError as e:
            print(f"Error parsing API response as JSON: {e}")
            debug_log(f"Response text: {response.text[:500]}...")
            create_error_output("JSON parsing error", str(e), response.text[:500])
            exit(1)
        
        publications = data.get("response", {}).get("docs", [])
        
        if not publications:
            print("No publications found")
            debug_log("API returned empty publications list")
            # Create empty array to avoid errors in the frontend
            processed_publications = []
        else:
            print(f"Found {len(publications)} publications")
            debug_log(f"First publication: {json.dumps(publications[0])[:500]}...")
            
            # Process the publications
            processed_publications = []
            for pub in publications:
                # Extract and format the data
                title = pub.get("title", ["Unknown Title"])[0] if pub.get("title") else "Unknown Title"
                
                # Process authors
                authors = pub.get("author", [])
                if len(authors) > 5:
                    author_text = f"{', '.join(authors[:3])}, et al."
                else:
                    author_text = ", ".join(authors)
                
                # Format journal info
                year = pub.get("year", "")
                journal = pub.get("pub", "")
                volume = pub.get("volume", "")
                page = pub.get("page", [""])[0] if pub.get("page") else ""
                
                journal_info = ""
                if journal:
                    journal_info += journal
                    if volume:
                        journal_info += f", {volume}"
                    if page:
                        journal_info += f", {page}"
                
                if year:
                    journal_info += f" ({year})"
                
                # Get links
                bibcode = pub.get("bibcode", "")
                ads_link = f"https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract" if bibcode else ""
                
                # Check for arXiv identifier
                arxiv_id = None
                identifiers = pub.get("identifier", [])
                for identifier in identifiers:
                    if identifier.startswith("arXiv:"):
                        arxiv_id = identifier.replace("arXiv:", "")
                        break
                
                arxiv_link = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""
                
                # Get citation and read counts
                citation_count = pub.get("citation_count", 0)
                read_count = pub.get("read_count", 0)
                
                # Create publication entry
                publication = {
                    "title": title,
                    "authors": author_text,
                    "journal_info": journal_info,
                    "year": year,
                    "ads_link": ads_link,
                    "arxiv_link": arxiv_link,
                    "citation_count": citation_count,
                    "read_count": read_count
                }
                
                processed_publications.append(publication)
        
        # Calculate stats before saving
        summary_stats = calculate_summary_stats(processed_publications)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        # Save the result with summary stats
        output_data = {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "summary_stats": summary_stats,
            "publications": processed_publications
        }
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"Saved {len(processed_publications)} publications to {OUTPUT_FILE}")
        debug_log("Script completed successfully")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        create_error_output("Unexpected error", str(e), traceback.format_exc())
        exit(1)

def create_error_output(error_type, error_message, details=""):
    """Create a JSON file with error information."""
    error_publications = [
        {
            "title": f"Error: {error_type}",
            "authors": "Please check GitHub Actions logs for details",
            "journal_info": f"Error message: {error_message}",
            "year": datetime.now().year,
            "ads_link": "https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586",
            "arxiv_link": "https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header",
            "is_first_author": False
        }
    ]
    
    error_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary_stats": calculate_summary_stats(error_publications),
        "error": {
            "type": error_type,
            "message": error_message,
            "details": details
        },
        "publications": error_publications
    }
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(error_data, f, ensure_ascii=False, indent=2)
        print(f"Created error output file at {OUTPUT_FILE}")
    except Exception as e:
        print(f"Failed to create error output file: {e}")

if __name__ == "__main__":
    main() 