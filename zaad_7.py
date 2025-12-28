import requests
from typing import List, Optional

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


def get_breweries_from_api() -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}  # get first 20
    response = requests.get(url, params=params)
    response.raise_for_status()  # raise error if request failed
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


def main():
    breweries_data = get_breweries_from_api()
    breweries_objects = brewery_factory(breweries_data)

    for brewery in breweries_objects:
        print(brewery)


if __name__ == "__main__":
    main()
