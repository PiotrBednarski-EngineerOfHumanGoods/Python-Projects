# Twitter Joke Bot

Twitter Joke Bot is a simple bot that automatically posts jokes to Twitter every 6 hours. It uses OAuth for authentication with the Twitter API.

## Requirements

- Python 3.x
- Library: `requests_oauthlib`

## Installation

1. Clone the repository:

    git clone https://github.com/your-username/twitter-joke-bot.git
    cd twitter-joke-bot

2. Install the required library:

    pip install requests_oauthlib

3. Set up environment variables:

    export TWITTER_CONSUMER_KEY='your_consumer_key'
    export TWITTER_CONSUMER_SECRET='your_consumer_secret'

## Usage

1. Run the script:

    python twitter_joke_bot.py

2. During the first run, the script will prompt you to authorize the application on Twitter. Follow the instructions displayed on the screen.

3. The bot will automatically post jokes every 6 hours.

## Additional Information

- Twitter API keys (consumer_key and consumer_secret) should be stored in environment variables for security.
- The bot saves obtained access tokens in the `twitter_tokens.json` file to avoid re-authorization on every run.
- The index of the last posted joke is saved in the `last_joke_index.txt` file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

### MIT License Summary

- Permission: Users are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:
  - The original copyright notice and permission notice shall be included in all copies or substantial portions of the Software.
  - The software is provided "as is", without warranty of any kind.
