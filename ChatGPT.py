import discord
from discord.ext import commands
import openai

openai.api_key = "xXx" #API KEY https://platform.openai.com/account/api-keys
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.command()
async def chat(ctx, *, message):
    prompt = f"You: {message}\nBot:"

    # Mostrar estado "escribiendo"
    async with ctx.typing():
        

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
    await ctx.send(answer)

    # Restaurar el estado del bot
    await bot.change_presence(activity=None)

bot.run('xXX') #TOKEN BOT https://discord.com/developers/applications
