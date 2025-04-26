import webbrowser
from colorama import Fore # type: ignore

# It's Logo
logo = """"""""""███████╗░█████╗░░██████╗████████╗░██╗░░░░░░░██╗███████╗██████╗░
██╔════╝██╔══██╗██╔════╝╚══██╔══╝░██║░░██╗░░██║██╔════╝██╔══██╗
█████╗░░███████║╚█████╗░░░░██║░░░░╚██╗████╗██╔╝█████╗░░██████╦╝
██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░░░████╔═████║░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██████╔╝░░░██║░░░░░╚██╔╝░╚██╔╝░███████╗██████╦╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░"""""""""

def main():
# It's Prints 
    print(Fore.CYAN + logo)
    print()
    print(Fore.WHITE + ("Welcome to FASTWEB"))
    print()
    print("1. YouTube")
    print("2. Facebook")
    print("3. Instagram")
    print("4. Wikipedia")
    print("5. Reddit")
    print("6. ChatGPT")
    print("7. X(Twitter)")
    print("8. WhatsApp Web")
    print("9. Yahoo")
    print("10. DuckDuckGo")
    print("11. Amazon")
    print("12. Yahoo Japan")
    print("13. MSN")
    print("14. TikTok")
    print("15. Naver")
    print("16. Weather")
    print("17. Netflix")
    print("18. Fandom")
    print("19. Twitch")
    print("20. Discord ")

# It's Choice
    choice = input(Fore.CYAN + "Please choice WebSite: ")
# And this
    if choice == '1':
      webbrowser.open_new('https://www.youtube.com')

    if choice == '2':
      webbrowser.open_new('https://www.facebook.com/')

    if choice == '3':
      webbrowser.open_new('https://www.instagram.com/')

    if choice == '4':
      webbrowser.open_new('https://www.wikipedia.org/')

    if choice == '5':
      webbrowser.open_new('https://www.reddit.com/')

    if choice == '6':
      webbrowser.open_new('https://chatgpt.com/')

    if choice == '7':
      webbrowser.open_new('https://x.com/')

    if choice == '8':
      webbrowser.open_new('https://www.whatsapp.com/')

    if choice == '9':
      webbrowser.open_new('https://www.yahoo.com/')

    if choice == '10':
      webbrowser.open_new('https://duckduckgo.com/')

    if choice == '11':
      webbrowser.open_new('https://www.amazon.com/')

    if choice == '12':
      webbrowser.open_new('https://www.yahoo.co.jp/')

    if choice == '13':
      webbrowser.open_new('https://www.msn.com/')

    if choice == '14':
      webbrowser.open_new('https://www.tiktok.com/')
      
    if choice == '15':
      webbrowser.open_new('https://www.naver.com/')

    if choice == '16':
      webbrowser.open_new('https://weather.com/')

    if choice == '17':
      webbrowser.open_new('https://www.netflix.com/')

    if choice == '18':
      webbrowser.open_new('https://www.fandom.com/')

    if choice == '19':
      webbrowser.open_new('https://www.twitch.tv/')

    if choice == '20':
      webbrowser.open_new('https://discord.com/')
# Launch 
if __name__ == "__main__":
    main()