import requests
import json
from bs4 import BeautifulSoup

def extract_json(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/html",
        "Accept-Language": "en-US,en;q=0.9",
    }

    with requests.Session() as s:
        try:
            # Get cookies first if needed
            if "upwork.com" in url:
                s.get("https://www.upwork.com", headers=headers)
            
            response = s.get(url, headers=headers)
            response.raise_for_status()

            # Try direct JSON first
            try:
                return response.json()
            except json.JSONDecodeError:
                # Fallback to HTML parsing for embedded JSON
                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script', type='application/ld+json')
                if scripts:
                    return [json.loads(script.string) for script in scripts]
                return None

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

# Usage
if __name__ == "__main__":
    url = input("Enter URL: ")
    result = extract_json(url)
    
    if result:
        print("Found JSON:")
        print(json.dumps(result, indent=2))
    else:
        print("No JSON found")