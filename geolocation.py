import socket
import requests

def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return None

def get_geolocation(ip_address):
    api_key = "31d61165359ab7e16a9ac4aac1b3e541"
    url = f"https://api.ipstack.com/{ip_address}?access_key={api_key}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return {
            "country": data.get("country_name"),
            "region": data.get("region_name"),
            "city": data.get("city"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("time_zone"),
        }
    else:
        return None

domain_name = "unblog.fr" 
ip_address = get_ip_address(domain_name)
if ip_address:
    print(f"The IP address of {domain_name} is {ip_address}")
else:
    print(f"Failed to resolve the IP address for {domain_name}")

# geolocation_info = get_geolocation(ip_address)
# print("Geolocation Information:")
# print(geolocation_info)
