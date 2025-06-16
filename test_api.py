#!/usr/bin/env python3
import requests
import json

def test_love2d_api():
    """Test Love2D MediaWiki API to understand the response format."""
    api_url = "https://love2d.org/w/api.php"
    
    # Test 1: Get page list
    print("=== Test 1: Getting page list ===")
    params = {
        "action": "query",
        "list": "allpages",
        "format": "json",
        "aplimit": 5,
        "apprefix": "love"
    }
    
    response = requests.get(api_url, params=params)
    data = response.json()
    print(f"Status: {response.status_code}")
    print(f"Response keys: {list(data.keys())}")
    
    if "query" in data and "allpages" in data["query"]:
        pages = data["query"]["allpages"]
        print(f"Found {len(pages)} pages:")
        for page in pages[:3]:
            print(f"  - {page['title']} (ID: {page['pageid']})")
    
    # Test 2: Get content for 'love' page
    print("\n=== Test 2: Getting 'love' page content ===")
    test_title = "love"
    
    # Try different parameter combinations
    test_params = [
        {
            "action": "query",
            "format": "json",
            "titles": test_title,
            "prop": "extracts",
            "explaintext": "1"
        },
        {
            "action": "query",
            "format": "json",
            "titles": test_title,
            "prop": "extracts",
            "explaintext": "true"
        },
        {
            "action": "query",
            "format": "json",
            "titles": test_title,
            "prop": "wikitext"
        },
        {
            "action": "query",
            "format": "json",
            "titles": test_title,
            "prop": "revisions",
            "rvprop": "content"
        }
    ]
    
    for i, params in enumerate(test_params, 1):
        print(f"\n--- Test 2.{i}: {params} ---")
        response = requests.get(api_url, params=params)
        data = response.json()
        
        print(f"Status: {response.status_code}")
        if "warnings" in data:
            print(f"Warnings: {data['warnings']}")
        
        if "query" in data and "pages" in data["query"]:
            page_data = list(data["query"]["pages"].values())[0]
            print(f"Page keys: {list(page_data.keys())}")
            
            if "extract" in page_data:
                content = page_data["extract"]
                print(f"Content length: {len(content)}")
                print(f"Content preview: {content[:200]}...")
            elif "revisions" in page_data and page_data["revisions"]:
                content = page_data["revisions"][0].get("*", "")
                print(f"Revision content length: {len(content)}")
                print(f"Content preview: {content[:200]}...")
            else:
                print("No content found")
        else:
            print("No pages in response")

if __name__ == "__main__":
    test_love2d_api()