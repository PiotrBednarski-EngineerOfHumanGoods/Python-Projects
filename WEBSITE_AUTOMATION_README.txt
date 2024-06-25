# Website Automation Script

This Python script allows you to open a set of URLs in your default web browser based on a command-line argument. It can be used to quickly open frequently visited websites categorized by purpose, such as "work" and "personal".

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. Save the script to a file, e.g., `WEBSITE_AUTOMATION.py`.

2. Open a terminal or command prompt.

3. Run the script with the desired set name as an argument. For example, to open the "personal" set of websites:

    ```sh
    python WEBSITE_AUTOMATION.py personal
    ```

    To open the "work" set of websites:

    ```sh
    python WEBSITE_AUTOMATION.py work
    ```

## Available Sets

The following sets are predefined in the script:

- `work`
  - https://www.instagram.com
  - https://www.github.com
  - https://www.beatstars.com
  - https://www.google.com
  - https://www.youtube.com
  - https://www.chatgpt.com

- `personal`
  - https://www.netflix.com
  - https://www.spotify.com
  - https://www.youtube.com

## Adding New Sets

To add new sets or modify existing ones, edit the `URLS` dictionary in the script:

```python
URLS = {
    "work": ["https://www.instagram.com", "https://www.github.com", "https://www.beatstars.com", "https://www.google.com", "https://www.youtube.com", "https://www.chatgpt.com"],
    "personal": ["https://www.netflix.com", "https://www.spotify.com", "https://www.youtube.com"],
    "new_set": ["https://example.com"]
}
