import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url):
    """
    Downloads an image from a given URL and saves it to Fetched_Images/
    Returns the saved file path or None if failed.
    """

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image (with headers to mimic respectful browser request)
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check if the content type is an image
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"✗ The URL does not point to an image: {url}")
            return None

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If no filename in URL, create one from hash
            filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}")
            return filepath

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        return None
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        return None


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs at once
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
