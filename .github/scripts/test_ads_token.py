#!/usr/bin/env python3
"""
Script to test the ADS API token.
This is a diagnostic script to verify that the token works properly.
"""

import os
import requests
import json
import sys

# Configuration
TEST_URL = "https://api.adsabs.harvard.edu/v1/search/query"
PARAMS = {
    "q": "author:kurtz",  # A simple query that should return results
    "fl": "title",        # Only get titles to keep the response small
    "rows": 3             # Limit to 3 results
}

def main():
    # Get the ADS token from environment variables
    ads_token = os.environ.get("ADS_TOKEN")
    if not ads_token:
        print("Error: ADS_TOKEN environment variable not set")
        sys.exit(1)
    
    print(f"Token found, length: {len(ads_token)}")
    print(f"Token starts with: {ads_token[:4]}...")
    
    # Prepare the API request
    headers = {
        "Authorization": f"Bearer {ads_token}",
        "Content-Type": "application/json"
    }
    
    # Make the API request
    print(f"Testing ADS API with a simple query...")
    
    try:
        response = requests.get(TEST_URL, headers=headers, params=PARAMS, timeout=30)
        
        print(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API request successful!")
            data = response.json()
            num_found = data.get("response", {}).get("numFound", 0)
            print(f"Query returned {num_found} results")
            
            # Print a few results for verification
            docs = data.get("response", {}).get("docs", [])
            if docs:
                print("\nSample results:")
                for i, doc in enumerate(docs[:3]):
                    print(f"{i+1}. {doc.get('title', ['No title'])[0]}")
            
            print("\nYour ADS token is working correctly!")
        else:
            print("❌ API request failed!")
            print(f"Response: {response.text}")
            
            # Check for common error codes
            if response.status_code == 401:
                print("\nError 401: Unauthorized. This means your token is invalid or expired.")
                print("Please generate a new token at https://ui.adsabs.harvard.edu/user/settings/token")
            elif response.status_code == 403:
                print("\nError 403: Forbidden. This means your token doesn't have the necessary permissions.")
                print("Make sure you're using a token with the right scope.")
            elif response.status_code == 429:
                print("\nError 429: Too Many Requests. You've hit the rate limit.")
                print("Try again later or request a higher rate limit.")
            
    except Exception as e:
        print(f"❌ Error making API request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 