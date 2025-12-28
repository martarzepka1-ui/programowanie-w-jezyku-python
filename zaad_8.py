from typing import List, Optional
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: str,
        state: str,
        postal_code: str,
        country: str,
        phone: Optional[str],
        website_url: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Brewery {self.name} ({self.brewery_type})\n"
            f"Address: {self.street or 'N/A'}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
            f"Phone: {self.phone or 'N/A'}\n"
            f"Website: {self.website_url or 'N/A'}\n"
        )

def get_breweries_from_api(city: Optional[str] = None) -> list:
    params = {"per_page": 20}
    if city:
        params["by_city"] = city
    response = requests.get(URL_API, params=params)
    response.raise_for_status()
    return response.json()

def brewery_factory(breweries: list) -> List[Brewery]:
    brewery_list = []
    for b in breweries:
        brewery_obj = Brewery(
            id=b.get("id"),
            name=b.get("name"),
            brewery_type=b.get("brewery_type"),
            street=b.get("street"),
            city=b.get("city"),
            state=b.get("state"),
            postal_code=b.get("postal_code"),
            country=b.get("country"),
            phone=b.get("phone"),
            website_url=b.get("website_url")
        )
        brewery_list.append(brewery_obj)
    return brewery_list

def get_args():
    parser = argparse.ArgumentParser(description='Fetch breweries from OpenBreweryDB')
    parser.add_argument('-c', '--city', help='Filter brewery by city', required=False)
    return vars(parser.parse_args())

def main():
    args = get_args()
    breweries_data = get_breweries_from_api(city=args['city'])
    breweries_objects = brewery_factory(breweries_data)

    for brewery in breweries_objects:
        print(brewery)

if __name__ == "__main__":
    main()
