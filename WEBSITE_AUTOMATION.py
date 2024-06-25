import sys
import webbrowser
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary of URLs categorized by 'work' and 'personal'
URLS = {
    "work": ["https://www.instagram.com", "https://www.github.com", "https://www.beatstars.com", "https://www.google.com", "https://www.youtube.com", "https://www.chatgpt.com"],
    "personal": ["https://www.netflix.com", "https://www.spotify.com", "https://www.youtube.com"]
}

def open_webpages(urls):
    """
    Opens a list of URLs in new browser tabs.
    
    Args:
    urls (list): List of URLs to open.
    """
    for url in urls:
        try:
            webbrowser.open_new_tab(url)
            logging.info(f"Opened {url}")
        except Exception as e:
            logging.error(f"Failed to open {url}: {e}")

def main():
    """
    Main function to handle command-line arguments and open URLs.
    """
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print("Usage: python WEBSITE_AUTOMATION.py <set_name>")
        print("Available sets:")
        for set_name in URLS.keys():
            print(f"- {set_name}")
        sys.exit(1)
    
    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)

if __name__ == "__main__":
    main()
