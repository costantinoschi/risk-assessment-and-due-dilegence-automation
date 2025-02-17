import requests

def perform_background_check(company_name):
    """
    Perform a background check using a third-party API.
    """
    # Example: Use a mock API for background checks
    api_url = f"https://api.example.com/background-check?company={company_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve background check data"}