import discord
from discord.ext import commands
import openai

openai.api_key = "Xxx" #API KEY https://platform.openai.com/account/api-keys
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')
    # Obtener el canal específico por su ID
    channel = bot.get_channel(1112191051709550692)
    if channel:
        await channel.send("¡Bot conectado y listo para responder!")

@bot.event
async def on_message(message):
    if message.channel.id == 1112191051709550692:
        if message.author == bot.user:
            return

        prompt = f"You: {message.content}\nBot:"

        # Mostrar estado "escribiendo"
        async with message.channel.typing():
            # Procesar la respuesta
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=50,
                temperature=0.7,
                n=1,
                stop=None,
            )

        # Obtener respuesta y enviarla al canal de Discord
        answer = response.choices[0].text.strip()
        await message.channel.send(answer)

    await bot.process_commands(message)


@bot.command()
async def limpiar_mensajes(ctx, amount: int):
    channel = ctx.channel
    await channel.purge(limit=amount)


bot.run('Xxx') #TOKEN BOT https://discord.com/developers/applications


