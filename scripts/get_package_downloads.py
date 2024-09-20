import requests

package_names = [
    "dscript",
    "conplex-dti",
    "fastdsd",
]

# Using Pepy.Tech API (https://www.pepy.tech/pepy-api)
API_ENDPOINT = "https://api.pepy.tech/api/v2/projects/{}"

def get_downloads(package):
    package_endpoint = API_ENDPOINT.format(package)
    r = requests.get(package_endpoint, headers = {"X-Api-Key": API_KEY})
    return r.json()["total_downloads"]

if __name__ == "__main__":
    API_KEY = input("API Key:")
    
    for package in package_names:
        print(f"{package}: {get_downloads(package)}")


