import whois
def get_whois_lookup(input):
    """Perform a WHOIS lookup for the given domain or IP."""
    try:
        whois_data = whois.whois(input)
        return dict(whois_data)  # Convert to dictionary
    except Exception as e:
        return {"Error": f"WHOIS lookup failed: {str(e)}"}
