# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:15:35 2024

@author: michaelalexander
"""

import requests
from bs4 import BeautifulSoup

def scrape_vehicle_data(url):
    """Scrape data kendaraan dari url Oto.com

    Args:
        url (str): URL dari listing kendaraan di Oto.com

    Returns:
        dict: Dictionary berisi scraped data kalau ada, atau None bila tidak berhasil.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Identify elements containing vehicle details (adapt selectors as needed)
        title_element = soup.find('h1', class_='title')
        price_element = soup.find('span', class_='price')
        # Add selectors for other desired data points (e.g., mileage, features)

        if title_element and price_element:
            data = {
                'title': title_element.text.strip(),
                'price': price_element.text.strip(),
                # Add other data keys and values here
            }
            return data
        else:
            print(f"Failed to extract data from {url}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Example usage (replace with actual oto.com listing URLs)
url1 = "https://www.oto.com/mobil-bekas/toyota-avanza-veloz-2019-jakarta- selatan-id-2222222"
url2 = "https://www.oto.com/motor-bekas/honda-beat-street-2020-bandung- id-3333333"

vehicle_data1 = scrape_vehicle_data(url1)
vehicle_data2 = scrape_vehicle_data(url2)

if vehicle_data1:
    print(vehicle_data1)

if vehicle_data2:
    print(vehicle_data2)