
from urllib.parse import urlparse
import re


def inspect_url(raw_url):
    findings = []
    url = raw_url.strip()

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Malformed URL. Check the URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains 5 or more hostname segments.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP instead of HTTPS.")

    return findings


def main():
    print("=" * 44)
    print("EWB Phishing URL Awareness Checker")
    print("Text-only checks; URLs are never opened.")
    print("Type 'q' to quit.")
    print("=" * 44)

    while True:
        raw_url = input("\nEnter a sample URL: ").strip()

        if raw_url.lower() == "q":
            print("Exiting checker.")
            break

        findings = inspect_url(raw_url)

        if findings:
            print("\nREVIEW CAREFULLY:")
            for finding in findings:
                print("- " + finding)
            print(f"Warning signs found: {len(findings)}")
        else:
            print("No listed warning signs found.")
            print("This does NOT prove the URL is safe.")


if __name__ == "__main__":
    main()
