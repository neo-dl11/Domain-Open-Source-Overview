import sys
import sublist3r

def get_subdomains(domain):
    try:
        subdomains = sublist3r.main(domain, 40, savefile=None, ports= None, silent=False, verbose=True, enable_bruteforce= False, engines=None)
        return subdomains

    except Exception as e:
        print(f"Error retrieving subdomains for {domain}: {e}")
        return []

if __name__ == "__main__":
    domain = sys.argv[1]
    subdomains = get_subdomains(domain)
