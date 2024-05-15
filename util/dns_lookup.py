import dns.resolver

def get_dns_lookup(input):
    """Perform a DNS lookup for the given domain to fetch various DNS records."""
    records = {}
    types_of_records = ['A', 'AAAA', 'CNAME', 'NS', 'MX', 'TXT']
    
    for record_type in types_of_records:
        try:
            answers = dns.resolver.resolve(input, record_type)
            records[record_type] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            records[record_type] = ["No records found"]
        except dns.resolver.NXDOMAIN:
            records['Error'] = f"DNS lookup failed: Domain {input} does not exist"
            return records
        except dns.resolver.Timeout:
            records['Error'] = "DNS query timed out"
            return records
        except Exception as e:
            records['Error'] = f"DNS lookup exception: {str(e)}"
            return records

    return records
