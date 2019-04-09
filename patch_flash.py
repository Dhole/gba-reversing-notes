#!/usr/bin/env python3

import subprocess
import sys
import r2pipe
from shutil import copyfile
from keystone import Ks, KS_ARCH_ARM, KS_MODE_ARM

gba_flash_patch_path = 'gba_flash.patch'
gba_flash_patch_size = 0xbf0

gba_flash_patch_addr = 0x8f80000
flash2ram_addr = 0x8f80000
flash2ram_bx_addr = 0x08f80050
ram2flash_addr = 0x08f80055
ram2flash_last_ops_addr = 0x08f80058
ram2flash_bx_addr = 0x08f8006c
ram2flash1_bx_addr = 0x08f8017c

ram2flash0_addr = flash2ram_addr + gba_flash_patch_size
ram2flash1_addr = 0x08f80070

bx_flash2ram_hex = '004908475500f808'

new_size = 0x1000000


def asm(code, addr=0x0):
    ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)
    encoding, count = ks.asm(code, addr=addr)
    return encoding


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
r2.cmd(f'af @ {save_addr}')
save_ctx_info = r2.cmdj(f'afij @ {save_addr}')
save_ctx_size = save_ctx_info[0]['size']
print(f'+ save addr context is {save_ctx_size} bytes')

save_addr_asm = """
    .thumb
    push {{r1}}
    push {{lr}}
    ldr r1, ram2flash0
    bx r1
    {filler}
.align
ram2flash0:
    .word 0x{ram2flash0:08x}
""".format(
    ram2flash0=ram2flash0_addr+1,
    filler='nop' if save_addr % 4 == 0 else ''
)

# pD: print disassembly of N bytes
ops = r2.cmdj(f'pDj {save_ctx_size} @ {save_addr}')
print(f'> Overwritting ops at {hex(save_addr)} with jump to ram2flash0 routine '
      f'at {hex(ram2flash1_addr)}')
print('+ Original:')
ops_hex = ''
for op in ops:
    print(f'    {hex(op["offset"])}    {op["bytes"]}    {op["disasm"]}')
    ops_hex += op["bytes"]
print('+ Replacement:',
      ''.join([f'    {l}\n' for l in save_addr_asm.splitlines()]))
save_addr_code = asm(save_addr_asm, addr=save_addr)
save_addr_hex = ''.join(['{:02x}'.format(b) for b in save_addr_code])
if len(save_addr_code) > len(ops_hex)/2:
    print(f'! Replacement code ({len(save_addr_code)}) is longer '
          f'than original ({len(ops)})!')
    sys.exit(1)

# wx: write hex
r2.cmd(f'wx {save_addr_hex} @ {save_addr}')

# wx: write hex
# print(f'> Writing saved ops from {hex(save_addr)} at last opts of ram2flash'
#       f' at {hex(ram2flash_last_ops_addr)}',
#       r2.cmd(f'wx {ops_hex} @ {ram2flash_last_ops_addr}'))

# This didn't work because rasm2 and keystone emmit wrong ldr relative offsets
# and b offsets respectively.
# offset = ram2flash0_addr
# offset = 0x00
# base = offset + 12
# ops_asm = ''
# data_asm = ''
# data_idx = 0
# print(f'+ Translated asm from save addr to run at {hex(base)}:')
# for op in ops:
#     # print(op)
#     if 'jump' in op:
#         addr = op['jump']
#         new_addr = base + (addr - save_addr)
#         print('Change 0x{:x} to 0x{:x} in {}'.format(addr, new_addr,
#                                                      op['disasm']))
#         op['disasm'] = op['disasm'].replace('0x{:x}'.format(addr),
#                                             '0x{:x}'.format(new_addr))
#     if op['type'] == 'load':
#         addr = op['ptr']
#         # val = ''.join(['{:02x}'.format(b) for b in
#         #                r2.cmdj(f'pxj 4 @ {addr}')[::-1]])
#         val = '0x{:08x}'.format(r2.cmdj(f'pxwj 4 @ {addr}')[0])
#         data_asm += f'val{data_idx}:\n    .word {val}\n'
# 
#         op['disasm'] = op['disasm'].replace('[0x{:08x}]'.format(addr),
#                                             f'val{data_idx}')
#         data_idx += 1
# 
#     new_offset = base + (op['offset'] - save_addr)
#     print(f'    {hex(new_offset)}    {op["bytes"]}    {op["disasm"]}')
#     ops_asm += f'    {op["disasm"]}\n'
# 
# print()

# sys.exit(1)

ram2flash0_asm_a = """
    .thumb
    push {{r0, r2, r3, r4, r5, r6, r7}}
    ldr r1, [pc, 0x0c]
    bx r1
    pop {{r0, r2, r3, r4, r5, r6, r7}}
    pop {{r1}}
    mov lr, r1
    pop {{r1}}
    b 0x14
.align 4
    .int32 0x{ram2flash1:08x}
    mov r0, r0
""".format(
    ram2flash1=ram2flash1_addr,
)

# This didn't work because rasm2 and keystone emmit wrong ldr relative offsets
# and b offsets respectively.
# ram2flash0_asm = """
#     .thumb
#     push {{r0, r2, r3, r4, r5, r6, r7}}
#     ldr r1, ram2flash1
#     bx r1
#     pop {{r0, r2, r3, r4, r5, r6, r7}}
#     pop {{r1}}
# save_addr_ctx:
# {save_addr_ctx}
# .align 4
# ram2flash1:
#     .word 0x{ram2flash1:08x}
# {data_asm}
# """.format(
#     filler='' if save_addr % 4 == 0 else 'nop',
#     ram2flash1=ram2flash1_addr+1,
#     save_addr_ctx=ops_asm,
#     data_asm=data_asm,
# )
# keystone assembler emmits wrong "b addr"
# ram2flash0_code = asm(ram2flash0_asm, addr=offset)
# ram2flash0_hex = ''.join(['{:02x}'.format(b) for b in ram2flash0_code])

# rasm2 emmits wrong relative offsets in ldr ops
ram2flash0_hex_a = subprocess.check_output(
        ['rasm2', '-a', 'arm', '-@', '-0x00',
            ram2flash0_asm_a.replace('\n', '; ')]).decode('ascii')[:-1]
# ram2flash0_hex = 'fdb4dff822100847fdbc02bc011c002900d0002001e0dff826000180012002bc08475600f80882050003'
# ram2flash0_hex = 'fdb4dff8121c0847fdbc02bc011c002900d0002001e0dff8160c0180012002bc08475600f80882050003'

print('ram2flash0_asm_a:\n', ram2flash0_asm_a)
print('ram2flash0_hex_a:\n', ram2flash0_hex_a)

# wx: write hex
print(f'> Writing routine at {hex(ram2flash0_addr)} to save regs, '
      f'jump to ram2flash1 at {hex(ram2flash1_addr)} ',
      # f'do ops from save addr at {hex(save_addr)}',
      r2.cmd(f'wx {ram2flash0_hex_a} @ {ram2flash0_addr}'))


ops_addr = ram2flash0_addr + len(ram2flash0_hex_a)//2
print(f'> Writing ops from save addr at {hex(ops_addr)}',
      r2.cmd(f'wx {ops_hex} @ {ops_addr}'))

base = ops_addr
# Read values loaded at ops and rewrite them at the relative address of
# ops_addr
for op in ops:
    if op['type'] == 'load':
        addr = op['ptr']
        val = '0x{:08x}'.format(r2.cmdj(f'pxwj 4 @ {addr}')[0])
        new_addr = base + (addr - save_addr)
        r2.cmd(f'wv4 {val} @ {new_addr}')

# wv4: write 32 bit value honoring endianness
# print(f'> Writing ram2flash return to address at {hex(ram2flash_bx_addr)}'
#       f' with {hex(save_addr+9)}',
#       r2.cmd(f'wv4 {save_addr+9} @ {ram2flash_bx_addr}'))

# wv4: write 32 bit value honoring endianness
print(f'> Writing ram2flash1 return to address at {hex(ram2flash1_bx_addr)}'
      f' with {hex(ram2flash0_addr+7)}',
      r2.cmd(f'wv4 {ram2flash0_addr+7} @ {ram2flash1_bx_addr}'))
# X + 8
