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
            "fl": "title,author,year,bibcode,pub,volume,page,doi,arxiv_class,identifier",
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
                
                # Create publication entry
                publication = {
                    "title": title,
                    "authors": author_text,
                    "journal_info": journal_info,
                    "year": year,
                    "ads_link": ads_link,
                    "arxiv_link": arxiv_link
                }
                
                processed_publications.append(publication)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        # Save the result
        output_data = {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
    error_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "error": {
            "type": error_type,
            "message": error_message,
            "details": details
        },
        "publications": [
            {
                "title": f"Error: {error_type}",
                "authors": "Please check GitHub Actions logs for details",
                "journal_info": f"Error message: {error_message}",
                "year": datetime.now().year,
                "ads_link": "https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586",
                "arxiv_link": "https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header"
            }
        ]
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