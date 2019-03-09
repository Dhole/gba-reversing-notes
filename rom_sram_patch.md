# Notes

- About flash carts patching: hypothesis is that the patch makes the rom work with SRAM.
- 0x100 is the entry point in GBA roms.

# Patches

https://gbatemp.net/threads/reverse-engineering-gba-patching.60168/

Save Pattern Blocks for Flash1M_V102
Unpatched block 1 (48 Bytes)
($aa,$21,$19,$70,$05,$4a,$55,$21,$11,$70,$b0,$21,$19,$70,
$e0,$21,$09,$05,$08,$70,$70,$47,$55,$55,$00,$0e,$aa,$2a,$00,$0e,
$30,$b5,$91,$b0,$68,$46,$00,$f0,$f3,$f8,$6d,$46,$01,$35,$06,$4a,
$aa,$20)

Patch with (136 Bytes)
($80,$21,$09,$02,$09,$22,$12,$06,$9f,$44,$11,$80,$03,$49,
$c3,$02,$c9,$18,$11,$80,$70,$47,$fe,$ff,$ff,$01,$00,$00,$00,$00,
$30,$b5,$91,$b0,$68,$46,$00,$f0,$f3,$f8,$6d,$46,$01,$35,$06,$4a,
$aa,$20,$00,$00,$05,$49,$55,$20,$00,$00,$90,$20,$00,$00,$10,$a9,
$03,$4a,$10,$1c,$08,$e0,$00,$00,$55,$55,$00,$0e,$aa,$2a,$00,$0e,
$20,$4e,$00,$00,$08,$88,$01,$38,$08,$80,$08,$88,$00,$28,$f9,$d1,
$0c,$48,$13,$20,$13,$20,$00,$06,$04,$0c,$e0,$20,$00,$05,$62,$20,
$62,$20,$00,$06,$00,$0e,$04,$43,$07,$49,$aa,$20,$00,$00,$07,$4a,
$55,$20,$00,$00,$f0,$20,$00,$00,$00,$00)

Unpatched Block 2 (24 Bytes)
($14,$49,$aa,$24,$0c,$70,$13,$4b,$55,$22,$1a,$70,$80,$20,$08,$70,
$0c,$70,$1a,$70,$10,$20,$08,$70)
Patch with
($0e,$21,$09,$06,$ff,$24,$80,$22,$13,$4b,$52,$02,$01,$3a,$8c,$54,
$fc,$d1,$00,$00,$00,$00,$00,$00)

Unpatched Block 3 (22 Bytes)
($aa,$25,$0d,$70,$13,$4b,$55,$22,$1a,$70,$80,$20,$08,$70,$0d,$70,
$1a,$70,$30,$20,$20,$70)
Patch with
($ff,$25,$08,$22,$00,$00,$52,$02,$01,$3a,$a5,$54,$fc,$d1,$00,$00,
$00,$00,$00,$00,$00,$00)

Unpatched Block 4 (12 Bytes)
($22,$70,$09,$4b,$55,$22,$1a,$70,$a0,$22,$22,$70)
Patch with
($00,$00,$09,$4b,$55,$22,$00,$00,$a0,$22,$00,$00)

Save Pattern Blocks for Flash1M_V103
Unpatched Block 1 (98 Bytes)
($05,$4b,$aa,$21,$19,$70,$05,$4a,$55,$21,$11,$70,$b0,$21,$19,$70,
$e0,$21,$09,$05,$08,$70,$70,$47,$55,$55,$00,$0e,$aa,$2a,$00,$0e,
$30,$b5,$91,$b0,$68,$46,$00,$f0,$f3,$f8,$6d,$46,$01,$35,$06,$4a,
$aa,$20,$10,$70,$05,$49,$55,$20,$08,$70,$90,$20,$10,$70,$10,$a9,
$03,$4a,$10,$1c,$08,$e0,$00,$00,$55,$55,$00,$0e,$aa,$2a,$00,$0e,
$20,$4e,$00,$00,$08,$88,$01,$38,$08,$80,$08,$88,$00,$28,$f9,$d1,
$0c,$48)
Patch with (138 Bytes)
($05,$4b,$80,$21,$09,$02,$09,$22,$12,$06,$9f,$44,$11,$80,$03,$49,
$c3,$02,$c9,$18,$11,$80,$70,$47,$fe,$ff,$ff,$01,$00,$00,$00,$00,
$30,$b5,$91,$b0,$68,$46,$00,$f0,$f3,$f8,$6d,$46,$01,$35,$06,$4a,
$aa,$20,$00,$00,$05,$49,$55,$20,$00,$00,$90,$20,$00,$00,$10,$a9,
$03,$4a,$10,$1c,$08,$e0,$00,$00,$55,$55,$00,$0e,$aa,$2a,$00,$0e,
$20,$4e,$00,$00,$08,$88,$01,$38,$08,$80,$08,$88,$00,$28,$f9,$d1,
$0c,$48,$13,$20,$13,$20,$00,$06,$04,$0c,$e0,$20,$00,$05,$62,$20,
$62,$20,$00,$06,$00,$0e,$04,$43,$07,$49,$aa,$20,$00,$00,$07,$4a,
$55,$20,$00,$00,$f0,$20,$00,$00,$00,$00)

Unpatched block 2 (24 bytes)
($14,$49,$aa,$24,$0c,$70,$13,$4b,$55,$22,$1a,$70,$80,$20,$08,$70,
$0c,$70,$1a,$70,$10,$20,$08,$70)
Patch with
($0e,$21,$09,$06,$ff,$24,$80,$22,$13,$4b,$52,$02,$01,$3a,$8c,$54,
$fc,$d1,$00,$00,$00,$00,$00,$00)

Unpatched block 3 (22 Bytes)
($aa,$25,$0d,$70,$14,$4b,$55,$22,$1a,$70,$80,$20,$08,$70,$0d,$70,
$1a,$70,$30,$20,$20,$70)
Patch with
($ff,$25,$08,$22,$00,$00,$52,$02,$01,$3a,$a5,$54,$fc,$d1,$00,$00,
$00,$00,$00,$00,$00,$00)

Unpatched block 4 (12 Bytes)
($10,$70,$0b,$49,$55,$20,$08,$70,$a0,$20,$10,$70)
Patch with
($00,$00,$0b,$49,$55,$20,$00,$00,$a0,$20,$00,$00)

Unpatched block 5 (12 bytes)
($22,$70,$09,$4b,$55,$22,$1a,$70,$a0,$22,$22,$70)
Patch with
($00,$00,$09,$4b,$55,$22,$00,$00,$a0,$22,$00,$00)


Save Pattern Blocks for Flash512_V130, V131, V133
Unpatched block 1 (38 Bytes)
($f0,$b5,$a0,$b0,$0d,$1c,$16,$1c,$1f,$1c,$03,$04,$1c,$0c,$0f,$4a,
$10,$88,$0f,$49,$08,$40,$03,$21,$08,$43,$10,$80,$0d,$48,$00,$68,
$01,$68,$80,$20,$80,$02)
Patch with
($70,$b5,$a0,$b0,$00,$03,$40,$18,$e0,$21,$09,$05,$09,$18,$08,$78,
$10,$70,$01,$3b,$01,$32,$01,$31,$00,$2b,$f8,$d1,$00,$20,$20,$b0,
$70,$bc,$02,$bc,$08,$47);

Unpatched block 2 (8 Bytes)
($ff,$f7,$88,$fd,$00,$04,$03,$0c)
Patch with
($1b,$23,$1b,$02,$32,$20,$03,$43)

Unpatched block 3 (8 Bytes)
($70,$b5,$90,$b0,$15,$4d,$29,$88)
Patch with
($00,$b5,$00,$20,$02,$bc,$08,$47)

Unpatched block 4 (8 Bytes)
($70,$b5,$46,$46,$40,$b4,$90,$b0)
Patch with
($00,$b5,$00,$20,$02,$bc,$08,$47)

Unpatched block 5 (24 Bytes)
($f0,$b5,$90,$b0,$0f,$1c,$00,$04,$04,$0c,$03,$48,
$00,$68,$40,$89,$84,$42,$05,$d3,$01,$48,$41,$e0)
Patch with (42 Bytes)
($7c,$b5,$90,$b0,$00,$03,$0a,$1c,$e0,$21,$09,$05,
$09,$18,$01,$23,$1b,$03,$10,$78,$08,$70,$01,$3b,
$01,$32,$01,$31,$00,$2b,$f8,$d1,$00,$20,$10,$b0,
$7c,$bc,$02,$bc,$08,$47);

Save Pattern Block for Eeprom_V120-V122
Unpatched Block 1 (20 Bytes)
($a2,$b0,$0d,$1c,$00,$04,$03,$0c,$03,$48,$00,$68,$80,$88,$83,$42,$05,$d3,$01,$48,$48,$e0)
Patch with (38 Bytes)
($00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$08,$78,$10,$70,$01,$33,
$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Unpatched Block 2 (22 Bytes)
($30,$b5,$a9,$b0,$0d,$1c,$00,$04,$04,$0c,$03,$48,$00,$68,$80,$88,$84,$42,$05,$d3,$01,$48,
$59,$e0)
Patch with (40 Bytes)
($70,$b5,$00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$10,$78,$08,$70,
$01,$33,$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Save Pattern Block for Eeprom_V124
Unpatched Block 1 (20 Bytes)
($a2,$b0,$0d,$1c,$00,$04,$03,$0c,$03,$48,$00,$68,$80,$88,$83,$42,$05,$d3,$01,$48,$48,$e0)
Patch with (38 Bytes)
($00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$08,$78,$10,$70,$01,$33,
$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Unpatched Block 2 (22 Bytes)
($f0,$b5,$ac,$b0,$0d,$1c,$00,$04,$01,$0c,$12,$06,$17,$0e,$03,$48,$00,$68,$80,$88,$81,$42,
$05,$d3)
Patch with (40 Bytes)
($70,$b5,$00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$10,$78,$08,$70,
$01,$33,$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Save Pattern Blocks for Eeprom_V126
Unpatched Block 1 (20 Bytes)
($a2,$b0,$0d,$1c,$00,$04,$03,$0c,$03,$48,$00,$68,$80,$88,$83,$42,$05,$d3,$01,$48,$48,$e0)
Patch with (38 Bytes)
($00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$08,$78,$10,$70,$01,$33,
$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Unpatched Block 2 (22 Bytes)
($f0,$b5,$47,$46,$80,$b4,$ac,$b0,$0e,$1c,$00,$04,$05,$0c,$12,$06,$12,$0e,$90,$46,$03,$48,
$00,$68)
Patch with (40 Bytes)
($70,$b5,$00,$04,$0a,$1c,$40,$0b,$e0,$21,$09,$05,$41,$18,$07,$31,$00,$23,$10,$78,$08,$70,
$01,$33,$01,$32,$01,$39,$07,$2b,$f8,$d9,$00,$20,$70,$bc,$02,$bc,$08,$47)

Save Pattern Block for Flash_v120 + Flash_v121
Unpatched Block 1 (12 Bytes)
($90,$b5,$93,$b0,$6f,$46,$39,$1d,$08,$1c,$00,$f0);
Patch with (14 Bytes)
($00,$b5,$3d,$20,$00,$02,$1f,$21,$08,$43,$02,$bc,$08,$47);

Unpatched Block 2 (35 Bytes)
($80,$b5,$94,$b0,$6f,$46,$39,$1c,$08,$80,$38,$1c,$01,$88,$0f,$29,$04,$d9,$01,$48,$56,$e0,$00,
$00,$ff,$80,$00,$00,$23,$48,$23,$49,$0a,$88,$23)
Patch with (36 bytes)
($7c,$b5,$00,$07,$00,$0c,$e0,$21,$09,$05,$09,$18,$01,$23,$1b,$03,$ff,$20,$08,$70,$01,$3b,$01, $31,$00,$2b,$fa,$d1,$00,$20,$7c,$bc,$02,$bc,$08,$47)

Unpatched Block 3 (42 Bytes)
($80,$b5,$94,$b0,$6f,$46,$79,$60,$39,$1c,$08,$80,$38,$1c,$01,$88,$0f,$29,$03,$d9,$00,$48,$73,
$e0,$ff,$80,$00,$00,$38,$1c,$01,$88,$08,$1c,$ff,$f7,$21,$fe,$39,$1c,$0c,$31)
Patch with
($7c,$b5,$90,$b0,$00,$03,$0a,$1c,$e0,$21,$09,$05,$09,$18,$01,$23,$1b,$03,$10,$78,$08,$70,$01,
$3b,$01,$32,$01,$31,$00,$2b,$f8,$d1,$00,$20,$10,$b0,$7c,$bc,$08,$bc,$08,$47)

Save Pattern Block for Flash_v123 + Flash_v124
Unpatched block 1 (8 Bytes)
($ff,$f7,$aa,$ff,$00,$04,$03,$0c)
Patch with
($1b,$23,$1b,$02,$32,$20,$03,$43)

Unpatched block 2 (6 Bytes)
($70,$b5,$90,$b0,$15,$4d)
Patch with
($00,$20,$70,$47,$15,$4d)

Unpatched block 3 (6 Bytes)
($70,$b5,$46,$46,$40,$b4)
Patch with
($00,$20,$70,$47,$40,$b4)

Unpatched block 4 (38 Bytes)
($f0,$b5,$90,$b0,$0f,$1c,$00,$04,$04,$0c,$0f,$2c,$04,$d9,$01,$48,$40,$e0,$00,$00,$ff,
$80,$00,$00,$20,$1c,$ff,$f7,$d7,$fe,$00,$04,$05,$0c,$00,$2d,$35,$d1)
Patch with
($70,$b5,$00,$03,$0a,$1c,$e0,$21,$09,$05,$41,$18,$01,$23,$1b,$03,$10,$78,$08,$70,$01,
$3b,$01,$32,$01,$31,$00,$2b,$f8,$d1,$00,$20,$70,$bc,$02,$bc,$08,$47)

Save Pattern Block for Flash_v125 + Flash_v126
Unpatched block 1 (8 Bytes)
($ff,$f7,$aa,$ff,$00,$04,$03,$0c)
Patch with
($1b,$23,$1b,$02,$32,$20,$03,$43);

Unpatched block 2 (6 Bytes)
($00,$03,$70,$b5,$90,$b0,$15,$4d)
Patch with
($00,$03,$00,$20,$70,$47,$15,$4d)

Unpatched block 3 (6 Bytes)
($00,$03,$70,$b5,$46,$46,$40,$b4)
Patch with
($00,$03,$00,$20,$70,$47,$40,$b4)

Unpatched block 4 (38 Bytes)
($f0,$b5,$90,$b0,$0f,$1c,$00,$04,$04,$0c,$0f,$2c,$04,$d9,$01,$48,$40,$e0,$00,$00,$ff,
$80,$00,$00,$20,$1c,$ff,$f7,$d7,$fe,$00,$04,$05,$0c,$00,$2d,$35,$d1)
Patch with
($70,$b5,$00,$03,$0a,$1c,$e0,$21,$09,$05,$41,$18,$01,$23,$1b,$03,$10,$78,$08,$70,$01,
$3b,$01,$32,$01,$31,$00,$2b,$f8,$d1,$00,$20,$70,$bc,$02,$bc,$08,$47)

---

Save Pattern Block for Eeprom_V111
Unpatched block 1 (8 Bytes)
($0e,$48,$39,$68,$01,$60,$0e,$48)
Patch with
($00,$48,$00,$47,$XX,$XX,$XX,$08) (See below for what to fill the XXs with)

Unpatched block 2 (8 Bytes)
($27,$e0,$d0,$20,$00,$05,$01,$88)
Patch with
($27,$e0,$e0,$20,$00,$05,$01,$88)

Patch block 3 (188 Bytes) (goes at the end of the rom data, see notes below)
($39,$68,$27,$48,$81,$42,$23,$d0,$89,$1c,$08,$88,$01,$28,$02,$d1,
$24,$48,$78,$60,$33,$e0,$00,$23,$00,$22,$89,$1c,$10,$b4,$01,$24,
$08,$68,$20,$40,$5b,$00,$03,$43,$89,$1c,$52,$1c,$06,$2a,$f7,$d1,
$10,$bc,$39,$60,$db,$01,$02,$20,$00,$02,$1b,$18,$0e,$20,$00,$06,
$1b,$18,$7b,$60,$39,$1c,$08,$31,$08,$88,$09,$38,$08,$80,$16,$e0,
$15,$49,$00,$23,$00,$22,$10,$b4,$01,$24,$08,$68,$20,$40,$5b,$00,
$03,$43,$89,$1c,$52,$1c,$06,$2a,$f7,$d1,$10,$bc,$db,$01,$02,$20,
$00,$02,$1b,$18,$0e,$20,$00,$06,$1b,$18,$08,$3b,$3b,$60,$0b,$48,
$39,$68,$01,$60,$0a,$48,$79,$68,$01,$60,$0a,$48,$39,$1c,$08,$31,
$0a,$88,$80,$21,$09,$06,$0a,$43,$02,$60,$07,$48,$00,$47,$00,$00,
$00,$00,$00,$0d,$00,$00,$00,$0e,$04,$00,$00,$0e,$d4,$00,$00,$04,
$d8,$00,$00,$04,$dc,$00,$00,$04,$XX,$XX,$XX,$08)

Notes
This ones a little trickier than the rest of them. I've managed to compact all the other save types into one patching routine but for this I've had to use a completely different patching routine. As you can see from the patch blocks there's a couple of non-standard bytes in Patch block 1 and Patch block 3. Patch block 2 is a simple search and patch routine, I'll explain about blocks 1 and 2 below. Before you begin your patching for this save type you have to calculate where the end of the actual rom data is as Patch block 3 needs to bea appended to the empty space after. Unfortunately though it's not as simple as jus fnding the first free byte, the patch has to begin in the first empty byte divisible by 16 (no remainder, in Pascal it's EOFMarker MOD 16 = 0). Make sure that this number is kept in a 32-bit number as your going to need the first 3 bytes of it! [​IMG]

Patch block 1
The unpatched search block 1 is standard between all roms so the same kind of search routines you used for all the others will do. Before patching the data though you need to fill in bytes 5,6 and 7 of the patch block. This data needs to be the first 3 bytes of the 32 bit number that you stored the EOF position in. The number that you should be patching in is the EOF marker position you stored earlier plus 1. So if the patch starts at file position 3000000 you need to apply the number 300001.

The way I did it in Pascal (there's probably an easier way) is to move the Integer into an 4 byte array (call it TmpArray for ease) and then copy the relevant bytes from that array into the patch data. So if the patch data is stored as an 8 byte array called PatchArray the code would simply be PatchArray[5] := TmpArray[1] and PatchArray[6] := TmpArray[2] and so on. Then it's just a simple matter of pasting the modified patch data in there. Keep a marker of the byte position of the start of this data as you'll need it to fill in the relevant data in patch block 3.

Patch block 3
Patch block 3 is actually pretty easy as there's no data to search for to overwrite with the patch, it's simply added in the empty space at the end of the rom. It has to be placed in the first position after the end of the rom data that's divisible by 16 (it has to be 16 byte aligned) or the rom won't be able to access the save data.

You need to modify bytes 185, 186 and 187 in the patch block. Again it's another offset and it's a 3 byte length number (a 24-bit number) the same as in patch block 1. Alter the data in this patch block exactly the same way that you altered the data in patch block 1. The number you need to fill bytes 185-187 with is the offset of patch 1 + 32 bytes. So if patch 1 is store at file offset 30000 the number you need to fill bytes 185-187 with would be 30032. Again the way I did it was just to move the 32 bit number I had the file offset + 32 stored in into an array of bytes and then copied the relevant bytes into the patch data. Once you've filled bytes 185-187 with the correct data you can just patch the data directly into the file.

Just as a side note, if the file is already trimmed by a trimmer the easiest thing to do would be to append 512 bytes of blank data to the end of the rom and then run your patching routine like normal.


Save Pattern Block for Eeprom_V120-V122

(20 Bytes)
a2b00d1c0004030c034800688088834205d3014848e0
->
(38 Bytes)
00040a1c400be021090541180731002308781070013301320139072bf8d9002070bc02bc0847

(22 Bytes)
30b5a9b00d1c0004040c034800688088844205d3014859e0
->
(40 Bytes)
70b500040a1c400be021090541180731002310780870013301320139072bf8d9002070bc02bc0847
