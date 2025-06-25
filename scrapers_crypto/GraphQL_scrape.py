import requests
import json
import pandas as pd

# Configure based on browser devtools observations
API_URL = "https://api.hotstreak.gg/graphql"  # Verify in Network tab
HEADERS = {
    "Authorization": "Bearer [FIND_ACTUAL_TOKEN_IN_NETWORK_REQUESTS]",
    "Content-Type": "application/json"
}

# Extract GraphQL query structure from browser devtools
QUERY = """
query ExtendedPlayerQuery($sport: SportType!, $date: String) {
  players(sport: $sport, date: $date) {
    edges {
      node {
        id
        name
        stats {
          rebounds
          points
          assists
          # Add all visible stats from UI
        }
        historicalPerformance {
          last10Games {
            date
            opponent
            # Add nested fields
          }
        }
        # Monitor network requests for hidden fields
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""

def fetch_players(sport="NBA", cursor=None):
    variables = {
        "sport": sport,
        "after": cursor
    }

    payload = {
        "operationName": "ExtendedPlayerQuery",
        "query": QUERY,
        "variables": variables
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}")
        return None

def scrape_all_players():
    all_players = []
    cursor = None
    has_next = True

    while has_next:
        data = fetch_players(cursor=cursor)
        if not data:
            break
            
        # Process nodes
        edges = data['data']['players']['edges']
        all_players.extend([edge['node'] for edge in edges])

        # Pagination
        page_info = data['data']['players']['pageInfo']
        has_next = page_info['hasNextPage']
        cursor = page_info['endCursor']

    return pd.DataFrame(all_players)

if __name__ == "__main__":
    df = scrape_all_players()
    df.to_excel("hotstreak_players.xlsx", index=False)
    print(f"Saved {len(df)} player records")