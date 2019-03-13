# Notes

- About flash carts patching: hypothesis is that the patch makes the rom work with SRAM.
- 0x100 is the entry point in GBA roms.

# Patches

https://gbatemp.net/threads/reverse-engineering-gba-patching.60168/

Save Pattern Blocks for Flash1M_V102
Unpatched block 1 (48 Bytes)
(aa211970054a55211170b0211970
e0210905087070475555000eaa2a000e
30b591b0684600f0f3f86d460135064a
aa20)

Patch with (136 Bytes)
(80210902092212069f4411800349
c302c91811807047feffff0100000000
30b591b0684600f0f3f86d460135064a
aa2000000549552000009020000010a9
034a101c08e000005555000eaa2a000e
204e000008880138088008880028f9d1
0c48132013200006040ce02000056220
62200006000e04430749aa200000074a
55200000f02000000000)

Unpatched Block 2 (24 Bytes)
(1449aa240c70134b55221a7080200870
0c701a7010200870)
Patch with
(0e210906ff248022134b5202013a8c54
fcd1000000000000)

Unpatched Block 3 (22 Bytes)
(aa250d70134b55221a70802008700d70
1a7030202070)
Patch with
(ff25082200005202013aa554fcd10000
000000000000)

Unpatched Block 4 (12 Bytes)
(2270094b55221a70a0222270)
Patch with
(0000094b55220000a0220000)

Save Pattern Blocks for Flash1M_V103
Unpatched Block 1 (98 Bytes)
(054baa211970054a55211170b0211970
e0210905087070475555000eaa2a000e
30b591b0684600f0f3f86d460135064a
aa2010700549552008709020107010a9
034a101c08e000005555000eaa2a000e
204e000008880138088008880028f9d1
0c48)
Patch with (138 Bytes)
(054b80210902092212069f4411800349
c302c91811807047feffff0100000000
30b591b0684600f0f3f86d460135064a
aa2000000549552000009020000010a9
034a101c08e000005555000eaa2a000e
204e000008880138088008880028f9d1
0c48132013200006040ce02000056220
62200006000e04430749aa200000074a
55200000f02000000000)

Unpatched block 2 (24 bytes)
(1449aa240c70134b55221a7080200870
0c701a7010200870)
Patch with
(0e210906ff248022134b5202013a8c54
fcd1000000000000)

Unpatched block 3 (22 Bytes)
(aa250d70144b55221a70802008700d70
1a7030202070)
Patch with
(ff25082200005202013aa554fcd10000
000000000000)

Unpatched block 4 (12 Bytes)
(10700b4955200870a0201070)
Patch with
(00000b4955200000a0200000)

Unpatched block 5 (12 bytes)
(2270094b55221a70a0222270)
Patch with
(0000094b55220000a0220000)


Save Pattern Blocks for Flash512_V130 V131 V133
Unpatched block 1 (38 Bytes)
(f0b5a0b00d1c161c1f1c03041c0c0f4a
10880f4908400321084310800d480068
016880208002)
Patch with
(70b5a0b000034018e021090509180878
1070013b01320131002bf8d1002020b0
70bc02bc0847);

Unpatched block 2 (8 Bytes)
(fff788fd0004030c)
Patch with
(1b231b0232200343)

Unpatched block 3 (8 Bytes)
(70b590b0154d2988)
Patch with
(00b5002002bc0847)

Unpatched block 4 (8 Bytes)
(70b5464640b490b0)
Patch with
(00b5002002bc0847)

Unpatched block 5 (24 Bytes)
(f0b590b00f1c0004040c0348
00684089844205d3014841e0)
Patch with (42 Bytes)
(7cb590b000030a1ce0210905
091801231b0310780870013b
01320131002bf8d1002010b0
7cbc02bc0847);

Save Pattern Block for Eeprom_V120-V122
Unpatched Block 1 (20 Bytes)
(a2b00d1c0004030c034800688088834205d3014848e0)
Patch with (38 Bytes)
(00040a1c400be0210905411807310023087810700133
01320139072bf8d9002070bc02bc0847)

Unpatched Block 2 (22 Bytes)
(30b5a9b00d1c0004040c034800688088844205d30148
59e0)
Patch with (40 Bytes)
(70b500040a1c400be021090541180731002310780870
013301320139072bf8d9002070bc02bc0847)

Save Pattern Block for Eeprom_V124
Unpatched Block 1 (20 Bytes)
(a2b00d1c0004030c034800688088834205d3014848e0)
Patch with (38 Bytes)
(00040a1c400be0210905411807310023087810700133
01320139072bf8d9002070bc02bc0847)

Unpatched Block 2 (22 Bytes)
(f0b5acb00d1c0004010c1206170e0348006880888142
05d3)
Patch with (40 Bytes)
(70b500040a1c400be021090541180731002310780870
013301320139072bf8d9002070bc02bc0847)

Save Pattern Blocks for Eeprom_V126
Unpatched Block 1 (20 Bytes)
(a2b00d1c0004030c034800688088834205d3014848e0)
Patch with (38 Bytes)
(00040a1c400be0210905411807310023087810700133
01320139072bf8d9002070bc02bc0847)

Unpatched Block 2 (22 Bytes)
(f0b5474680b4acb00e1c0004050c1206120e90460348
0068)
Patch with (40 Bytes)
(70b500040a1c400be021090541180731002310780870
013301320139072bf8d9002070bc02bc0847)

Save Pattern Block for Flash_v120 + Flash_v121
Unpatched Block 1 (12 Bytes)
(90b593b06f46391d081c00f0);
Patch with (14 Bytes)
(00b53d2000021f21084302bc0847);

Unpatched Block 2 (35 Bytes)
(80b594b06f46391c0880381c01880f2904d9014856e000
00ff800000234823490a8823)
Patch with (36 bytes)
(7cb50007000ce0210905091801231b03ff200870013b01 31002bfad100207cbc02bc0847)

Unpatched Block 3 (42 Bytes)
(80b594b06f467960391c0880381c01880f2903d9004873
e0ff800000381c0188081cfff721fe391c0c31)
Patch with
(7cb590b000030a1ce0210905091801231b031078087001
3b01320131002bf8d1002010b07cbc08bc0847)

Save Pattern Block for Flash_v123 + Flash_v124
Unpatched block 1 (8 Bytes)
(fff7aaff0004030c)
Patch with
(1b231b0232200343)

Unpatched block 2 (6 Bytes)
(70b590b0154d)
Patch with
(00207047154d)

Unpatched block 3 (6 Bytes)
(70b5464640b4)
Patch with
(0020704740b4)

Unpatched block 4 (38 Bytes)
(f0b590b00f1c0004040c0f2c04d9014840e00000ff
800000201cfff7d7fe0004050c002d35d1)
Patch with
(70b500030a1ce0210905411801231b031078087001
3b01320131002bf8d1002070bc02bc0847)

Save Pattern Block for Flash_v125 + Flash_v126
Unpatched block 1 (8 Bytes)
(fff7aaff0004030c)
Patch with
(1b231b0232200343);

Unpatched block 2 (6 Bytes)
(000370b590b0154d)
Patch with
(000300207047154d)

Unpatched block 3 (6 Bytes)
(000370b5464640b4)
Patch with
(00030020704740b4)

Unpatched block 4 (38 Bytes)
(f0b590b00f1c0004040c0f2c04d9014840e00000ff
800000201cfff7d7fe0004050c002d35d1)
Patch with
(70b500030a1ce0210905411801231b031078087001
3b01320131002bf8d1002070bc02bc0847)

---

Save Pattern Block for Eeprom_V111
Unpatched block 1 (8 Bytes)
(0e48396801600e48)
Patch with
(00480047XXXXXX08) (See below for what to fill the XXs with)

Unpatched block 2 (8 Bytes)
(27e0d02000050188)
Patch with
(27e0e02000050188)

Patch block 3 (188 Bytes) (goes at the end of the rom data see notes below)
(39682748814223d0891c0888012802d1
2448786033e000230022891c10b40124
086820405b000343891c521c062af7d1
10bc3960db01022000021b180e200006
1b187b60391c083108880938088016e0
15490023002210b40124086820405b00
0343891c521c062af7d110bcdb010220
00021b180e2000061b18083b3b600b48
396801600a48796801600a48391c0831
0a88802109060a430260074800470000
0000000d0000000e0400000ed4000004
d8000004dc000004XXXXXX08)

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
a2b00d1c0004030c034800688088834205d30148__e0
->
(38 Bytes)
00040a1c400be021090541180731002308781070013301320139072bf8d9002070bc02bc0847

(22 Bytes)
30b5a9b00d1c0004040c034800688088844205d30148__e0
->
(40 Bytes)
70b500040a1c400be021090541180731002310780870013301320139072bf8d9002070bc02bc0847

# Save Pattern Block for Eeprom_V124

## A (22 B)
a2b00d1c0004030c034800688088834205d3014848e0
->
00040a1c400be021090541180731002308781070013301320139072bf8d9002070bc02bc0847

## B (24 B)
f0b5acb00d1c0004010c1206170e034800688088814205d3
->
70b500040a1c400be021090541180731002310780870013301320139072bf8d9002070bc02bc0847

## Minish Cap:
A: 0x080b0b4a - 0x80b0b60 a2b00d1c0004030c034800688088834205d3014844e0
B: 0x080b0c0c - 0x80b0c24 f0b5acb00d1c0004010c1206170e034800688088814205d3

### Trace from A to 0x0807C83C

0x0807c80c ; reached at save
0x0807c838 -> 0x0807c92c
0x0807c83c
0x0807c85c -> 0x08f80055 ; SRAM to Flash patch
0x0807c876

0x0807c92c ; reached at save
0x0807c92e -> 0x0807c9ac
0x0807c932

0x0807c9ac ; reached at startup & at save
0x0807c9ec -> 0x0807cc30
0x0807c9f0
0x0807ca26

0x0807cc30
0x0807cc46 -> 0x080b0e3c
0x0807cc4a
0x0807cc6e

0x080b0e3c
0x080b0e56 -> 0x080b0e04
0x080b0e5a
0x080b0e78

0x080b0e04
0x080b0e20 -> 0x080b0c0c
0x080b0e24
0x080b0e34

0x080b0c0c ; patch B
0x080b0ca2 -> 0x80b0ac8
0x080b0ca6
0x080b0d6a

NOTE: the chinese bootleg has been patched with the Eeprom_V124 SRAM patch!
