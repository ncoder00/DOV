import socket
import requests

def get_geolocation(input):
    """Retrieve geolocation information for a given IP address or domain using ipinfo.io."""
    try:
        # Check if the input is a domain name and resolve it to an IP
        if not input.replace('.', '').isdigit():  # Simple check if it's an IP
            input = socket.gethostbyname(input)

        response = requests.get(f"https://ipinfo.io/{input}/json")
        if response.status_code == 200:
            return dict(response.json())  # Convert to dictionary
        else:
            return {"Error": f"Failed to retrieve data, status code: {response.status_code}"}
    except socket.gaierror:
        return {"Error": "DNS resolution failed, invalid domain"}
    except Exception as e:
        return {"Error": str(e)}