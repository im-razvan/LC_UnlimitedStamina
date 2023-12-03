# Made for game version 40
from pymem import *
from time import sleep

try:
    pm = Pymem('Lethal Company.exe')
    base = pymem.process.module_from_name(pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll
except:
    print('[!] Game not found.')
    input(); exit()

def GetAddr(base: int, offsets: tuple) -> int:
    address = pm.read_longlong(base)
    for i in offsets[:-1]:
        address = pm.read_longlong(address + i)
    return address + offsets[-1]

def main():
    print('[+] Unlimited Stamina Hack For Lethal Company (v40)')
    while True:
        try:
            staminaAddr = GetAddr(base + 0x751290, (0x210, 0x2A8, 0x420))
            pm.write_float(staminaAddr, 1.)
            print("[+] Stamina Address: {:x}".format(staminaAddr), end = f'{" "*15}\r')
        except:
            print("[+] Stamina Address: ??", end = f'{" "*15}\r')
        sleep(.25)

if __name__ == '__main__':
    main()