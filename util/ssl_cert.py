import ssl
import socket

def ssl_cert_details(domain):
    """Retrieve SSL certificate details for the given domain."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                # Extract specific fields from the certificate
                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])

                cert_details = {
                    "Subject": subject.get('commonName', 'Not Available'),
                    "Issuer": issuer.get('organizationName', 'Not Available'),
                    "ASN1 Curve": cert.get('asn1Curve', 'Not Available'),
                    "NIST Curve": cert.get('nistCurve', 'Not Available'),
                    "Expires": cert['notAfter'],
                    "Renewed": cert['notBefore'],
                    "Serial Num": cert['serialNumber'],
                }
                return cert_details

    except Exception as e:
        return {"Error": f"SSL certificate retrieval failed: {str(e)}"}