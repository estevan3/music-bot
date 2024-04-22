import discord
from discord.ext import commands
from os import getenv
import discord.ext.commands
from dotenv import load_dotenv
import yt_dlp


import discord.ext

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
playlist = []


def next_music(e, voice_channel):
    if len(playlist) > 0:
        playlist.pop(0)
        audio_stream(voice_channel)


def audio_stream(voice_channel):
    ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    ydl_opts = {'format': 'bestaudio'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist[0], download=False)
        voice_channel.play(
            discord.FFmpegPCMAudio(info["url"],
                                   **ffmpeg_options),
            after=lambda e: next_music(e, voice_channel))


@bot.event
async def on_ready():
    print(f"You are logged in as: {bot.user}")


@bot.command(name='play', help='Play a song from YouTube')
async def play(ctx: discord.ext.commands.Context, url: str):
    if not ctx.message.author.voice:
        await ctx.send('You are not connected to a voice channel!')
        return

    channel = ctx.message.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    playlist.append(url)
    if voice_client:
        if not voice_client.is_playing():
            audio_stream(voice_client)
    else:
        voice_channel = await channel.connect()
        audio_stream(voice_channel)


@bot.command(name='stop', help='To the music')
async def stop(ctx: discord.ext.commands.Context):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.send('Music stopped.')
    else:
        await ctx.send('No music is currently playing.')


@bot.command(name='disconnect', help='leaves the voice channel')
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

bot.run(getenv("TOKEN"))
