# Notes about radare2 usage

Disassemble hex string in arm thumb mode at offset:
```
 $ rasm2 -a arm -b 16 -@ 0x0807c85c -d '0349 4d81 0220 c871'
```

## In radare2 console

Set arm thumb mode (16 bits instructions):
```
ahb 16
```

Set arm mode (32 bits instructions):
```
ahb 32
```

Find hex string ignorign some nibbles:
```
/x a2b00d1c0004030c034800688088834205d30148..e0
```

Search for a string:
```
/ STRING
```

Print string at address:
```
ps @ addr
```

Disassemble N bytes at address, page the output:
```
pd N @ addr ~..
```

### Debugging

Start mgba with gdbserver:
```
mgba -g chinese_zelda_minish_cap.gba
```

Start radare2 attached to gdbserver:
```
r2 -a arm -b 32 -s 0x8000000 -D gdb -c "e dbg.bpinmaps=false" gdb://127.0.0.1:2345
```

```
L ningba.so ; Load GBA Plugin
e asm.arch=arm ; Set architecture to ARM
e asm.bits=16 ; Set ARM Thumb mode (16 bits)
```
