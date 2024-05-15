import re
import ipaddress

def is_valid_domain(domain):
    """Validate and sanitize domain format."""
    # Remove all spaces
    domain = domain.replace(" ", "")
    # Regular expression for domain validation
    pattern = r'^([a-zA-Z0-9-]+\.)*[a-zA-Z]{2,}$'
    return re.match(pattern, domain), domain

def is_valid_ip(ip):
    """Validate and sanitize IP address, also check for private IPs."""
    ip = ip.replace(" ", "")  # Strip spaces
    try:
        ip_obj = ipaddress.ip_address(ip)
        # Optionally, check if the IP is private
        if ip_obj.is_private:
            return False, ip  # Change to `True, ip` if private IPs should be valid
        return True, ip
    except ValueError:
        return False, ip
