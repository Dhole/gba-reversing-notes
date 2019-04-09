#!/usr/bin/env python3

from keystone import *

ram2flash0_addr = 0x08f80055
ram2flash1_addr = 0x08f80055

code1 = """
    .thumb
    push {{r1}}
    ldr r1, ram2flash0
    bx r1
    nop
ram2flash0:
    .word 0x{ram2flash0:08x}
""".format(
    ram2flash0 = ram2flash0_addr
)

# code1 = """
#     bl 0x{bx_addr:08x}
# """.format(
#     bx_addr = 0x08f80055
# )

code2 = """
    .thumb
    push {{r0, r2, r3, r4, r5, r6, r7}}
    ldr r1, ram2flash1
    bx r1
    pop {{r0, r2, r3, r4, r5, r6, r7}}
    pop {{r1}}
save_addr_ctx:
    .short 0x0123, 0x4567, 0x89ab, 0xcdef
.align
ram2flash1:
    .word 0x{ram2flash1:08x}
""".format(
    ram2flash1 = ram2flash1_addr,
    # save_addr_ctx = '0123456789abcdef'
    save_addr_ctx = '01234567'
)
# save_addr + len(bx_flash2ram)+1

code3 = """
    .thumb
    push {r0, r2, r3, r4, r5, r6, r7}
    ldr r1, ram2flash1
    bx r1
    pop {r0, r2, r3, r4, r5, r6, r7}
    pop {r1}
save_addr_ctx:
    adds r1, r0, 0
    cmp r1, 0
    beq 0x16
    movs r0, 0
    b 0x1c
    ldr r0, val0
    strh r1, [r0]
    movs r0, 1
    pop {r1}
    bx r1

.align 4
ram2flash1:
    .word 0x08f80056
val0:
    .word 0x03000582
"""

code = code3
addr = 0x00

# print(code)

ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)
encoding, count = ks.asm(code, addr=addr)

# print(encoding)
# print(count)

# for b in encoding:
#     print('{:02x} '.format(b), end='')
print(''.join(['{:02x} '.format(b) for b in encoding]))
