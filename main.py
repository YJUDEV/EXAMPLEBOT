import discord   #디스코드 라이브러리 사용선언
import time


token_file = open("C:\\Users\\yju08\\OneDrive\\동기화폴더\\서버용폴더\\예제봇\\private\\token.txt",encoding="utf-8") 
token = token_file.read()
token_file.close()

client = discord.Client()


# 프로그램이 처음 실행되었을 때 초기 구성
@client.event
async def on_ready():
    print("예제봇을 시작합니다")
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    print("===========")


# 봇에 메시지가 오면 수행 될 액션
@client.event
async def on_message(message):
    #봇이 보낸 메시지면 반응 안함
    if message.author.bot:
        return None


    if message.content == "!명령어":
        
        channel = message.channel

        embed = discord.Embed(title="명령어 안내", description="",color=0x5CD1E5)
        embed.add_field(name="!말해", value="채팅을 보내는 예제를 보여드려요", inline=False)
        embed.add_field(name="!임베드", value="임베드 예제를 보여드려요", inline=False)
        embed.add_field(name="!소스코드", value="소스코드 링크를 공유해드려요", inline=False)

        await channel.send(embed=embed)


    if message.content == "!말해":
        
        channel = message.channel
        await channel.send("말했습니다!")


    if message.content == "!임베드":
        channel = message.channel

        embed = discord.Embed(title="이것이 임베드입니다", description="하하하",color=0x5CD1E5)
        embed.add_field(name="1 임베드랍니다!", value="이게 임베드지", inline=False)
        embed.add_field(name="2 임베드랍니다!", value="이게 임베드지", inline=False)

        await channel.send(embed=embed)

    if message.content == "!소스코드":
        channel = message.channel
        await channel.send("해당링크를 참고하세요! :"+"")



client.run(token)