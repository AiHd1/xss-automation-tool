import requests
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_payloads(payload_file):
    """Load XSS payloads from a file."try:
        with open(payload_file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        logging.error(f"Payload file {payload_file} not found.")
        return []

def check_xss(url, payload):
    """Send a payload to the URL and check for XSS vulnerability."try:
        response = requests.get(url, params={'input': payload}, timeout=10)
        if payload in response.text:
            logging.warning(f"Potential XSS vulnerability detected with payload: {payload}")
            return True
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
    return False

def main(url, payload_file):
    """Main function to scan for XSS vulnerabilities."""
    payloads = load_payloads(payload_file)
    if not payloads:
        logging.error("No payloads to test.")
        return

    for payload in payloads:
        payload = payload.strip()
        if check_xss(url, payload):
            logging.info(f"Vulnerable to XSS with payload: {payload}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate XSS vulnerability scanning.")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--payloads", required=True, help="File containing XSS payloads")
    args = parser.parse_args()

    main(args.url, args.payloads)