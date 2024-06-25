import sys
import webbrowser

# Dictionary of URLs categorized by 'work' and 'personal'
URLS = {
    "work": ["https://www.instagram.com", "https://www.github.com", "https://www.beatstars.com", "https://www.google.com", "https://www.youtube.com", "https://www.chatgpt.com"],
    "personal": ["https://www.netflix.com", "https://www.spotify.com", "https://www.youtube.com"]
}

# Function to open a list of URLs in new browser tabs
def open_webpages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)  # Open each URL in a new browser tab

if __name__ == "__main__":
    # Check if the script received exactly one argument and if it matches any key in URLS
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print("Usage: python WEBSITE_AUTOMATION.py <set_name>")
        print("Available sets:")
        for set_name in URLS.keys():
            print(f"- {set_name}")  # Print available set names
        sys.exit(1)  # Exit the script with a status code of 1 indicating an error

    # Get the set name from the arguments and the corresponding URLs
    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)  # Open the URLs in the browser
