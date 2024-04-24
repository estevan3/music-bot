# Discord Music Bot

This project is a Discord bot designed to play music in voice channels. It uses the `discord.py` library for interacting with Discord's API and the `yt-dlp` library for streaming audio from YouTube.

## Prerequisites

Before you start, you will need to install the following software on your system:

- Python 3.10: The bot is written in Python, so you will need to have Python installed. [You can download it from the official Python website.](https://www.python.org/downloads/release/python-31011/)
  - For Linux go [here](https://python.org.br/instalacao-linux/)

## Setting Up the Bot on Discord

1. Go to the Discord Developer Portal and log in to your Discord account.
2. Click on “New Application”. Give your app a name and click “Create”.
3. In the side panel, click on “Bot” and then “Reset Token”. Confirm by clicking “Yes, do it!”.
4. In the “TOKEN” section, click “Copy”. This is your bot's token, which will be used to log in to the bot via code. Keep this token safe and do not share it with anyone.
5. Click on 'Bot' and select the options: PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT.
6. Paste the Token into the ".example.env" file under TOKEN="Your Token" and rename the file to ".env" .

## To Execute

- Run the "run.bat" file if you use Windows.
- Run the "run.sh" file if you use Linux or macOS.

## Add Bot on Discord Server

1. Return to the newly created bot dashboard.
2. Click on 'OAuth2' and check the 'bot' box.
3. Check the boxes: Read Messages/View Channels, Send Messages, Manage Messages, Read Message History, Connect, Speak.
4. In the 'Generated URL' section, click on 'Copy' and paste it into your browser's address bar.
5. Select a discord server click 'Continue' -> 'Authorize'.

## Features

- **Music Playback**: The bot can join a voice channel and play music from a YouTube URL. The music playback can be controlled with various commands.
- **Commands**: The bot supports several commands:
  - `.play [url]`: Plays music from the provided YouTube URL in the voice channel the user is currently connected to.
  - `.stop`: Stops the current music playback.
  - `.disconnect`: Disconnects the bot from the voice channel.
- **Environment Variables**: The bot uses environment variables for configuration, making it easy to deploy in different environments.

## Future Improvements

Future improvements could include adding pause and resume commands, and expanding the bot's capabilities to play music from other sources besides YouTube.
