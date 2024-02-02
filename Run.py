#!/usr/bin/env python3
import platform, subprocess
import os,sys
#os.system( 'f'xdg-open https://t.me/haxkx')

#os.system (f'xdg-open https://t.me/covidtrixcker')
os.system(f'xdg-open https://t.me/addlist/sCAXu_wpqXY1Nzhl')
if name == 'main':
    try:
        if platform.machine() == "aarch64":
            subprocess.call(["chmod", "+x", "aarch64"])
            subprocess.call(["./aarch64"])
        else:
            print(f"[Error] Not supported for device {platform.machine()}!")
            exit()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"[Error] {str(e).capitalize()}!")
        exit()
