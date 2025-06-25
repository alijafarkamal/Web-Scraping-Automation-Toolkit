import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


URLS = [
    'https://javedch.com/javed-chaudhry-urdu-columns',
    'https://javedch.com/javed-chaudhry-urdu-columns/page/2',
    'https://javedch.com/javed-chaudhry-urdu-columns/page/3',
    'https://javedch.com/javed-chaudhry-urdu-columns/page/4',
    'https://javedch.com/javed-chaudhry-urdu-columns/page/5'
]

def extract_contact_info(soup):
    """Extract contact details from a soup object"""
    records = []

    profiles = soup.select('.profile-card')  # Change this selector
    
    for profile in profiles:
        record = {
            'first': profile.select_one('.first-name').text.strip() if profile.select_one('.first-name') else '',
            'last': profile.select_one('.last-name').text.strip() if profile.select_one('.last-name') else '',
            'email': profile.select_one('a[href^="mailto:"]')['href'].replace('mailto:', '') if profile.select_one('a[href^="mailto:"]') else '',
            'phone': re.search(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}', profile.text).group() if re.search(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}', profile.text) else ''
        }
        records.append(record)
    return records

def scrape_site():
    all_data = []
    
    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            all_data.extend(extract_contact_info(soup))
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
    
    return pd.DataFrame(all_data)

def save_to_excel(df):
    df.to_excel('directory_contacts.xlsx', index=False)
    print("Excel file saved as directory_contacts.xlsx")

if __name__ == "__main__":
    contacts_df = scrape_site()
    save_to_excel(contacts_df)