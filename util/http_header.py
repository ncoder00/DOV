import requests

def get_http_headers(url):
    """Fetch HTTP headers for a given URL, attempting HTTPS first, then falling back to HTTP if necessary."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
        if response.headers:
            return dict(response.headers)  # Ensure headers are returned as a standard dictionary
        else:
            return {"Error": "No headers found"}
    except requests.exceptions.SSLError:
        try:
            url = url.replace('https://', 'http://') # Fallback to http
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
            if response.headers:
                return dict(response.headers)
            else:
                return {"Error": "No headers found after fallback to HTTP"}
        except requests.RequestException as e:
            return {"Error": f"HTTP request failed after fallback to HTTP: {str(e)}"}
    except requests.RequestException as e:
        return {"Error": f"HTTP request failed: {str(e)}"}