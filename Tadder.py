from sys import argv
from time import sleep
from os import system  as term
try:
    from platform import system
except:
    system("pip install platform")
#____________________________________________________________________________________

apiId = 123456 # The API ID of your Telegram account
apiHash = "pedaret123pedaret321" # The API Hash of your Telegram account

#____________________________________________________________________________________
blu = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"
res = "\033[0;m"

#____________________________________________________________________________________
help = f"""
    {red}Usage {ylw}: {grn}python Tadder.py [OPTION] ...
    {ylw}Adds members of another group to another group

    Mandatory arguments to long options are mandatory for short options too
        {red}-h {ylw}, {red}--help          {grn}display this help and exit
        {red}-e {ylw}, {red}--ex            {grn}member extraction
        {red}-a {ylw}, {red}--add           {grn}Add members

    {ylw}Use help 

        {red}[{blu}Extract{red}] {grn}python {red}Tadder.py {ylw}--ex{red}/{ylw}-e 
        {red}[{blu}Add{red}] {grn}python {red}Tadder.py {ylw}--add{red}/{ylw}-a {red}<{grn}Group Id{red}>

"""

asciiArt = f"""{red}
 ____   _       ____    __  __  _      _____   ___   __ __ 
|    \ | T     /    T  /  ]|  l/ ]    |     | /   \ |  T  T
|  o  )| |    Y  o  | /  / |  ' /     |   __jY     Y|  |  |
|     T| l___ |     |/  /  |    \     |  l_  |  O  |l_   _j
|  O  ||     T|  _  /   \_ |     Y    |   _] |     ||     |
|     ||     ||  |  \     ||  .  |    |  T   l     !|  |  |
l_____jl_____jl__j__j\____jl__j\_j    l__j    \___/ |__j__|
            {grn}Telegram {blu}:  {red}@BlackFoxSecurityTeam  
            {blu} Coded By MrB4rCod & Maximum Radikali
{res}"""

#____________________________________________________________________________________
def clear():
    sleep(0.2)
    if system() == "Windows":
        term('cls')
    elif system() == "Linux" or system() == "Darwin":
        term('clear')
#____________________________________________________________________________________
from telethon.sync import TelegramClient , events
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
import telethon
#____________________________________________________________________________________
client = TelegramClient("BlackFox" ,apiId,apiHash)
gp_lists = []
i = 0

#_________________________________{ Scraper }________________________________________
def Scraper():
    client.start()
    clear()
    print(asciiArt)
    global i
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group == True:
            try:
                if dialog.entity.username:
                    gp_lists.append(str(dialog.entity.username))
            except:
                continue
    
    for pla in gp_lists:
        i += 1
        print(f"{red}{str(i)} {blu}➜ {grn}{pla}")

    usgp = input(f"\n{red}❯❯{blu} ")
    users = client.get_participants(gp_lists[int(usgp)] , limit=5000)
    open("members.txt","w").write("")
    user_me = client.get_me().username
    for user in users:
        if user.username != None:
            if "bot" in user.username:
                continue
            else:
                if user_me == str(user.username):
                    pass
                else:
                    open("members.txt" , "a").write(str(user.username) + "\n")

    print (f"\n{blu}[{ylw}!{blu}] {red}Member has been fetched now ")
#__________________________________{ Adder }__________________________________________
def adder(gpId):
    client.start()
    clear()
    print(asciiArt)
    input_channel = client.get_entity(gpId) # blackfoxgroup
    user = open("members.txt","r")
    peer_channel = PeerChannel(input_channel.id)
    i = 0
    for userr in user:
        i += 1
        try:
            peer_user = client.get_input_entity(userr)
            client(InviteToChannelRequest(peer_channel,users=[peer_user]))
            username = userr.replace('\n'," ")
            print (f"{blu}[{red}{str(i)}{blu}] {grn}{username}")
        except telethon.errors.rpcerrorlist.UserPrivacyRestrictedError:
            print (f"{blu}[{red}-{blu}] {red}Error from user privacy {ylw}!")
            continue
        except telethon.errors.rpcerrorlist.PeerFloodError:
            print (f"{blu}[{red}-{blu}] {red}Error from Peer Flood {ylw}!")
            sleep(5)
            continue
        except telethon.errors.rpcerrorlist.FloodWaitError:
            print (f"{blu}[{ylw}!{blu}] {red}Wait for long time 20 min {ylw}!")
            sleep(60 * 20)
            continue
        except telethon.errors.rpcerrorlist.UserChannelsTooMuchError:
            continue
        except telethon.errors.rpcerrorlist.UserNotMutualContactError:
            continue
#____________________________________________________________________________________
if(len(argv) <= 1 ):
    clear()
    print(asciiArt)
    print(help)        
elif(len(argv) >= 1):
    if argv[1] == "--help" or argv[1] == "-h":
        clear()
        print(asciiArt)
        print(help)
    elif argv[1] == "--ex" or argv[1] == "-e":
        if (len(argv) <= 2):
            clear()
            Scraper()
        else:
            clear()
            print(asciiArt)
            print(help)
    elif argv[1] == "--add" or argv[1] == "-a":
        if (len(argv) <= 3):
            clear()
            adder(argv[2])
        else:
            clear()
            print(asciiArt)
            print(help)  
    else:
        clear()
        print(asciiArt)
        print(help)
