import random
import string 
import requests
import os
import time
import json
from colorama import Fore, init
import datetime
from configparser import ConfigParser
import sys

init(autoreset=True)

# Configuration & Globals
__version__ = "Author: suenerve DSV 1.9"
__github__= "https://github.com/suenerve"
dir_path = os.path.dirname(os.path.realpath(__file__))
configur = ConfigParser()
configur.read(os.path.join(dir_path, "config.ini"))
tokens_list = os.path.join(dir_path, "tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"

available_usernames = []
av_list = os.path.join(dir_path, "available_usernames.txt")
sample_0 = r"_."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTYELLOW_EX
Delay = configur.getfloat("config", "default_delay")

# Helper to set title on Windows and Termux/Linux
def set_terminal_title(title_str):
    if os.name == 'nt':
        os.system(f'title {title_str}')
    else:
        # Escape sequence for Linux/Termux terminals
        sys.stdout.write(f"\x1b]2;{title_str}\x07")
        sys.stdout.flush()

def s_sys_h():
    auth_token = ""
    if configur.getboolean("sys", "MULTI_TOKEN"):
        auth_token = avail_tokens(tokens_list)[integ_0]
    else:
        auth_token = configur.get("sys", "TOKEN")
    
    return {
        "Content-Type": "Application/json",
        "Orgin": "https://discord.com/",
        "Authorization": auth_token
    }

def sys_c_t():
    if configur.get("sys", "TOKEN") == "" and not configur.getboolean("sys", "MULTI_TOKEN"):
        print(f"{Lb}[!]{Fore.RED} No token found in config.ini")
        sys.exit()
    elif configur.getboolean("sys", "MULTI_TOKEN") and not avail_tokens(tokens_list):
        print(f"{Lb}[!]{Fore.RED} No tokens found in tokens.txt")
        sys.exit()

def setconf():
    global string_0, digits_0, punctuation_0, webhook_0, sat_string, sat_digits, sat_multi_token, sat_punct, sat_webhook
    sat_webhook = configur.get("sys", "WEBHOOK_URL")
    sat_string = configur.getboolean("config", "string")
    sat_digits = configur.getboolean("config", "digits")
    sat_punct = configur.getboolean("config", "punctuation")
    sat_multi_token = configur.getboolean("sys", "MULTI_TOKEN")
    
    webhook_0 = bool(sat_webhook)
    string_0 = string.ascii_lowercase if sat_string else ""
    digits_0 = string.digits if sat_digits else ""
    punctuation_0 = sample_0 if sat_punct else ""
    
    if not (sat_punct or sat_digits or sat_string):
        punctuation_0, digits_0, string_0 = sample_0, string.digits, string.ascii_lowercase

def main():
    sys_c_t()
    setconf()

    # Safely fetch username for the title
    try:
        res = requests.get(sys_url, headers=s_sys_h())
        res_data = res.json()
        user_display = res_data.get('username', 'Unknown')
        discrim = res_data.get('discriminator', '0000')
    except Exception:
        user_display = "Error"
        discrim = "0000"

    # Set Terminal Title (Works in Termux and Windows)
    set_terminal_title(f"{__version__} - Connected as {user_display}")

    print(f"""{Fore.LIGHTYELLOW_EX}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
  {__version__} 
  {__github__}                     {Fore.LIGHTCYAN_EX}Connected as {user_display}{Ly}#{Fore.LIGHTCYAN_EX}{discrim}{Ly}
                            
  ██████╗ ███████╗██╗   ██╗                     {Fore.LIGHTCYAN_EX}1-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate names and check{Fore.LIGHTBLACK_EX}]{Ly}             
  ██╔══██╗██╔════╝██║   ██║                     {Fore.LIGHTCYAN_EX}2-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Check a specific list{Fore.LIGHTBLACK_EX}]{Ly}             
  ██║  ██║███████╗██║   ██║                     
  ██║  ██║╚════██║╚██╗ ██╔╝                     Config.ini:
  ██████╔╝███████║ ╚████╔╝                        {Fore.LIGHTCYAN_EX}Digits: {Fore.YELLOW}{sat_digits}{Ly}
  ╚═════╝ ╚══════╝  ╚═══╝                         {Fore.LIGHTCYAN_EX}String: {Fore.YELLOW}{sat_string}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Punctuation: {Fore.YELLOW}{sat_punct}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Multi-Token: {Fore.YELLOW}{sat_multi_token}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Webhook: {Fore.YELLOW}{webhook_0}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Delay: {Fore.YELLOW}{Delay}{Ly}
                                                         
  Discord Username's availability validator.
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()

# ... [The rest of your functions: proc0, validate_names, etc., stay the same] ...
# Make sure they are correctly indented to the left margin (not inside main)
