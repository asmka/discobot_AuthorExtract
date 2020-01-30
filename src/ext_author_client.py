import sys
import discord


# Extract specific author's message and send to the specific channel
class ExtAuthorClient(discord.Client):
    _is_called_on_ready = False
    _author_id = None
    _channel_id = None
    _channel = None


    def __init__(self, author_id: str, channel_id: str):
        super().__init__()
        self._author_id = author_id
        self._channel_id = channel_id


    # on_ready is not necessarily called just once.
    # So, do process only at the first calling.
    async def on_ready(self):
        #print('on ready', flush=True)
        if not self._is_called_on_ready:
            self._channel = self.get_channel(self._channel_id)
            if not self._channel:
                print(f'[ERROR] Cannot find the channel with given id: {self._channel_id}', file=sys.stderr)
                sys.exit(1)
            self._is_called_on_ready = True


    async def on_message(self, msg):
        if msg.author.id == self._author_id:
            # Generate quoted message

            # Before:
            # aaa
            # bbb
            #
            # After:
            # > aaa
            # > bbb
            # https://...

            msg_url = f'https://discordapp.com/channels/{msg.guild.id}/{msg.channel.id}/{msg.id}'

            quoted_msg = '> ' + msg.content.replace('\n', '\n> ') + '\n'
            quoted_msg += msg_url

            await self._channel.send(quoted_msg)
