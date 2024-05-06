import requests

# API endpoint for random quotes
api_url = "https://api.quotable.io/random"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    quote_text = data["content"]
    quote_author = data["author"]

    print(f"\nQuote of the Day:\n{quote_text}\n  - {quote_author}")
else:
    print(f"Error: {response.status_code}")

"""
Explanation:

    1. We import requests.
    2. We define the api_url for the Quotable.io API's random quote endpoint.
    3. We send a GET request and capture the response.
    4. We check the status code.
    5. If successful (200), we parse the JSON response and extract:
        - quote_text from the "content" key (the actual quote).
        - quote_author from the "author" key (the author's name).
    6. We print the quote and author in a formatted way.

Remember:

    -Replace placeholders with the actual API URL if needed.
    -Consider rate limits or usage restrictions imposed by the API provider.
    -Explore the API documentation for available endpoints and data structures.

This example demonstrates how to use requests to retrieve data from a simple API and process it for user presentation. You can adapt this approach for various APIs that provide data in JSON format.
"""