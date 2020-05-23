import discord   #디스코드 라이브러리 사용선언
import time  #이건 시간 출력하려고 import함

#token을(디코봇 비밀번호? 그런거라거 생각하면됨) 파일에서 읽어오기
#굳이 파일에서 읽는 이유는 남들에게 보이면 안되는 데이터니까 그냥 코드에 넣을수는 없기 때문
token_file = open("C:\\Users\\yju08\\OneDrive\\동기화폴더\\서버용폴더\\예제봇\\private\\token.txt",encoding="utf-8") 
token = token_file.read()
token_file.close()

#client생성, 그냥 이렇게 하는구나.. 생각하면 됨 문법적으로 이해는 이 과목에선 힘듬
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

    #메시지가 !명령어면
    if message.content == "!명령어":
        channel = message.channel  #메시지가 보내진 채널정보를 담음

        #embed를 생성
        embed = discord.Embed(title="명령어 안내", description="",color=0x5CD1E5)
        embed.add_field(name="!말해", value="채팅을 보내는 예제를 보여드려요", inline=False)
        embed.add_field(name="!임베드", value="임베드 예제를 보여드려요", inline=False)
        embed.add_field(name="!소스코드", value="소스코드 링크를 공유해드려요", inline=False)

        #채널에 embed 전송
        await channel.send(embed=embed)

    #메시지가 !말해 면
    if message.content == "!말해":
        channel = message.channel  #메시지가 보내진 채널 정보를 담음
        await channel.send("말했습니다!")   #채널에 말했습니다! 전송


    #메시지가 !임베드 면
    if message.content == "!임베드":
        channel = message.channel #메시지가 보내진 채널 정보를 담음

        #임베드 생성
        embed = discord.Embed(title="이것이 임베드입니다", description="하하하",color=0x5CD1E5)
        embed.add_field(name="1 임베드랍니다!", value="이게 임베드지", inline=False)
        embed.add_field(name="2 임베드랍니다!", value="이게 임베드지", inline=False)

        #채널에 embed 전송
        await channel.send(embed=embed)

    #메시지가 !소스코드 면
    if message.content == "!소스코드":
        channel = message.channel  #메시지가 보내진 채널 정보를 담음
        await channel.send("해당링크를 참고하세요! :"+"https://github.com/YJUDEV/EXAMPLEBOT/blob/master/main.py")  #채널에 링크 전송



client.run(token)  #실행