import argparse
import json
import sys
from typing import Dict, Optional

import requests


def get_ip_info(ip: Optional[str] = None) -> Dict[str, str]:
    if ip:
        url = f"http://ip-api.com/json/{ip}"
    else:
        url = "http://ip-api.com/json/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "fail":
            raise ConnectionError(data.get("message", "Unknown error"))
        return {
            "ip": data.get("query", ""),
            "version": "IPv4",
            "city": data.get("city", ""),
            "region": data.get("regionName", ""),
            "country_name": data.get("country", ""),
            "country_code": data.get("countryCode", ""),
            "latitude": data.get("lat", ""),
            "longitude": data.get("lon", ""),
            "timezone": data.get("timezone", ""),
            "isp": data.get("isp", ""),
            "org": data.get("org", ""),
        }
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch IP info: {e}") from e


def format_output(data: Dict[str, str], json_output: bool = False) -> str:
    if json_output:
        return json.dumps(data, indent=2)

    lines = []
    if "ip" in data:
        lines.append(f"IP: {data['ip']}")
    if "version" in data:
        lines.append(f"Version: {data['version']}")
    if "city" in data and data["city"]:
        lines.append(f"City: {data['city']}")
    if "region" in data and data["region"]:
        lines.append(f"Region: {data['region']}")
    if "country_name" in data and data["country_name"]:
        lines.append(f"Country: {data['country_name']}")
    if "country_code" in data:
        lines.append(f"Country Code: {data['country_code']}")
    if "latitude" in data:
        lines.append(f"Latitude: {data['latitude']}")
    if "longitude" in data:
        lines.append(f"Longitude: {data['longitude']}")
    if "timezone" in data and data["timezone"]:
        lines.append(f"Timezone: {data['timezone']}")
    if "isp" in data and data["isp"]:
        lines.append(f"ISP: {data['isp']}")
    if "org" in data and data["org"]:
        lines.append(f"Organization: {data['org']}")

    return "\n".join(lines) if lines else "No data available"


def main():
    parser = argparse.ArgumentParser(description="IP Info CLI Tool")
    parser.add_argument("ip", nargs="?", help="IP address to lookup (omit for your own IP)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    try:
        data = get_ip_info(args.ip)
        if "error" in data:
            print(f"Error: {data.get('reason', 'Unknown error')}", file=sys.stderr)
            sys.exit(1)
        print(format_output(data, args.json))
    except ConnectionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
