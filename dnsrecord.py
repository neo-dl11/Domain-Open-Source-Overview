import dns.resolver

def get_dns_records(domain):
    dns_records = {}
    try:
        a_records = []
        for answer in dns.resolver.resolve(domain, 'A'):
            a_records.append(answer.to_text())
        dns_records['A_records'] = a_records

        mx_records = []
        for rdata in dns.resolver.resolve(domain, 'MX'):
            mx_records.append(rdata.exchange.to_text())
        dns_records['MX_records'] = mx_records

        txt_records = []
        for answer in dns.resolver.resolve(domain, 'TXT'):
            txt_records.append(answer.to_text())
        dns_records['TXT_records'] = txt_records

    except dns.resolver.NoAnswer:
        dns_records['error'] = "No DNS records found."
    except dns.resolver.NXDOMAIN:
        dns_records['error'] = "Domain does not exist."

    return dns_records

