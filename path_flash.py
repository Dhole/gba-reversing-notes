#!/usr/bin/env python3

import sys
import r2pipe
from shutil import copyfile

gba_flash_patch_path = 'gba_flash.patch'

gba_flash_patch_addr = 0x8f80000
flash2ram_addr = 0x8f80000
flash2ram_bx_addr = 0x08f80050
ram2flash_addr = 0x0
ram2flash_last_ops_addr = 0x08f80058
ram2flash_bx_addr = 0x08f8006c

bx_flash2ram_hex = '004908475500f808'

new_size = 0x1000000

filename = sys.argv[1]
filename_patch = sys.argv[2]
# save_addr = '0x08067ca4' # Zelda a Link to the Past
save_addr = int(sys.argv[3], 16)

copyfile(filename, filename_patch)

r2 = r2pipe.open(filename_patch, flags=['-w'])

entry = 0x8000000
op0 = r2.cmdj(f'pdj 1 @ {entry}')[0]
if 'jump' not in op0:
    print('! op at {entry} is not a jump')
op0_jump_addr = op0["jump"]
print(f'+ op0 jumps to {hex(op0_jump_addr)}')

file_size = r2.cmdj('ij')['bin']['binsz']
if file_size > new_size:
    print(f'! File is too big for this patch: {file_size/1024/1024} bytes')

print(f'> Extending file to {hex(new_size)} bytes',
      r2.cmd(f'r {new_size}'))

print(f'> Patching {hex(gba_flash_patch_addr)} with gba flash patch',
      r2.cmd(f'wff {gba_flash_patch_path} @ {gba_flash_patch_addr}'))

op_jump_flash2ram = f'b {flash2ram_addr}'
print(f'> Patching {hex(entry)} to jump to flash2ram routine at'
      f' {hex(flash2ram_addr)}',
      r2.cmd(f'wa {op_jump_flash2ram} @ {entry}'))

print(f'> Writing flash2ram return to address at {hex(flash2ram_bx_addr)}'
      f' with {hex(op0_jump_addr)}',
      r2.cmd(f'wv4 {op0_jump_addr} @ {flash2ram_bx_addr}'))

r2.cmd('e asm.bits=16')
r2.cmd(f'ahb 16 @ {save_addr}')
ops = r2.cmdj(f'pDj 8 @ {save_addr}')
print(f'> Overwritting ops at {hex(save_addr)} with jump to ram2flash routine'
      f'at {ram2flash_addr}')
ops_hex = ''
for op in ops:
    print(f'    {hex(op["offset"])}    {op["bytes"]}    {op["disasm"]}')
    ops_hex += op["bytes"]
r2.cmd(f'wx {bx_flash2ram_hex} @ {save_addr}')

print(f'> Writing saved ops from {hex(save_addr)} at last opts of ram2flash'
      f' at {hex(ram2flash_last_ops_addr)}',
      r2.cmd(f'wx {ops_hex} @ {ram2flash_last_ops_addr}'))

print(f'> Writing ram2flash return to address at {hex(ram2flash_bx_addr)}'
      f' with {hex(save_addr+9)}',
      r2.cmd(f'wv4 {save_addr+9} @ {ram2flash_bx_addr}'))

