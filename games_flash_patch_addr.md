# Legend of Zelda, The - A Link to the Past & Four Swords (USA, Australia)

- sha256sum: `f328f8f07d736288a00c80d31cc1630f3aa02aaf20efdcba73d31dae832b5d76`
- save addr: `0x08067ca4`

```
./patch_sram.py rom.gba /tmp/rom.sram.gba
./patch_flash.py /tmp/rom.sram.gba /tmp/rom.flash.gba 0x08067ca4
```
