#!/usr/bin/env python3

import sys
import r2pipe
from shutil import copyfile

gba_flash_patch_path = 'gba_flash.patch'
gba_flash_patch_size = 0xbf0

gba_flash_patch_addr = 0x8f80000
flash2ram_addr = 0x8f80000
flash2ram_bx_addr = 0x08f80050
ram2flash_addr = 0x08f80055
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
# pd: print disassembly
op0 = r2.cmdj(f'pdj 1 @ {entry}')[0]
if 'jump' not in op0:
    print('! op at {entry} is not a jump')
op0_jump_addr = op0["jump"]
print(f'+ op0 jumps to {hex(op0_jump_addr)}')

# i: file info
file_size = r2.cmdj('ij')['bin']['binsz']
if file_size > new_size:
    print(f'! File is too big for this patch: {file_size/1024/1024} bytes')
    sys.exit(1)

print(f'+ Checking for empty space in the gba flash patch area'
      f' ({hex(gba_flash_patch_addr)} -'
      f' {hex(gba_flash_patch_addr + gba_flash_patch_size)})')

# px: print hex
patch_area = r2.cmdj(f'pxj {gba_flash_patch_size} @ {gba_flash_patch_addr}')
if not (all(b == 0x00 for b in patch_area) or
        all(b == 0xff for b in patch_area)):
    print('!Not all bytes in the gba flash patch area are 0x00 nor 0xff')
    sys.exit(1)

# r: resize
print(f'> Extending file to {hex(new_size)} bytes',
      r2.cmd(f'r {new_size}'))

# wff: write contents of file
print(f'> Patching {hex(gba_flash_patch_addr)} with gba flash patch',
      r2.cmd(f'wff {gba_flash_patch_path} @ {gba_flash_patch_addr}'))

op_jump_flash2ram = f'b {flash2ram_addr}'
# wa: write opcode
print(f'> Patching {hex(entry)} to jump to flash2ram routine at'
      f' {hex(flash2ram_addr)}',
      r2.cmd(f'wa {op_jump_flash2ram} @ {entry}'))

# wv4: write 32 bit value honoring endianness
print(f'> Writing flash2ram return to address at {hex(flash2ram_bx_addr)}'
      f' with {hex(op0_jump_addr)}',
      r2.cmd(f'wv4 {op0_jump_addr} @ {flash2ram_bx_addr}'))

r2.cmd('e asm.bits=16')
# ahb: force N bits instructions
r2.cmd(f'ahb 16 @ {save_addr}')
# pD: print disassembly of N bytes
ops = r2.cmdj(f'pDj 8 @ {save_addr}')
print(f'> Overwritting ops at {hex(save_addr)} with jump to ram2flash routine '
      f'at {hex(ram2flash_addr)}')
ops_hex = ''
for op in ops:
    print(f'    {hex(op["offset"])}    {op["bytes"]}    {op["disasm"]}')
    ops_hex += op["bytes"]
# wx: write hex
r2.cmd(f'wx {bx_flash2ram_hex} @ {save_addr}')

# wx: write hex
print(f'> Writing saved ops from {hex(save_addr)} at last opts of ram2flash'
      f' at {hex(ram2flash_last_ops_addr)}',
      r2.cmd(f'wx {ops_hex} @ {ram2flash_last_ops_addr}'))

# wv4: write 32 bit value honoring endianness
print(f'> Writing ram2flash return to address at {hex(ram2flash_bx_addr)}'
      f' with {hex(save_addr+9)}',
      r2.cmd(f'wv4 {save_addr+9} @ {ram2flash_bx_addr}'))

