import requests

def extract_json_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        
        # Attempt to parse the response as JSON
        try:
            json_data = response.json()
            return json_data
        except ValueError:
            print("Error: The response does not contain valid JSON data.")
            return None
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    return None

# Example usage
if __name__ == "__main__":
    url = input("Enter the URL to extract JSON from: ")
    json_data = extract_json_from_url(url)
    
    if json_data is not None:
        print("Extracted JSON data:")
        print(json_data)
    else:
        print("Failed to extract JSON data.")