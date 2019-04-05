#!/usr/bin/env python3

from keystone import *

code1 = """
    ldr r1, ram2flash
    bx r1
ram2flash:
    .word 0x{bx_addr:08x}
""".format(
    bx_addr = 0x08f80055
)

# code1 = """
#     bl 0x{bx_addr:08x}
# """.format(
#     bx_addr = 0x08f80055
# )

code2 = """
    push {{r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12}}
    ldr r1, ram2flash
    bx r1
    pop {{r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12}}

    ldr r1, save_addr
    bx r1
ram2flash:
    .word 0x{bx_addr:08x}
save_addr:
    .word 0x{save_addr:08x}
""".format(
    bx_addr = 0x8f80070,
    save_addr = 0x12345678,
)
# save_addr + len(bx_flash2ram)+1

code = code2

print(code)

ks = Ks(KS_ARCH_ARM, KS_MODE_THUMB)
encoding, count = ks.asm(code)

for b in encoding:
    print('{:02x} '.format(b), end='')
print()
