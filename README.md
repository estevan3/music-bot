# Discord Music Bot

This project is a Discord bot designed to play music in voice channels. It uses the `discord.py` library for interacting with Discord's API and the `yt-dlp` library for streaming audio from YouTube.

## Features

- **Music Playback**: The bot can join a voice channel and play music from a YouTube URL. The music playback can be controlled with various commands.
- **Commands**: The bot supports several commands:
  - `!mplay [url]`: Plays music from the provided YouTube URL in the voice channel the user is currently connected to.
  - `!mstop`: Stops the current music playback.
  - `!disconnect`: Disconnects the bot from the voice channel.
- **Environment Variables**: The bot uses environment variables for configuration, making it easy to deploy in different environments.

## Future Improvements

Future improvements could include adding a queue system to line up multiple songs, adding pause and resume commands, and expanding the bot's capabilities to play music from other sources besides YouTube.
