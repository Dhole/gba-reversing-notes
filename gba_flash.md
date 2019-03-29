# Pattern 1
```
*0x000000 = 0x00ff
*0x000000 = 0x0090
```

## Kingdom Hearts

```
000000  8a 00 10 88 02 00 02 00  8a 00 cf bf 02 00 02 00  |................|
000010  8a 00 10 88 02 00 02 00  8a 00 cf bf 02 00 02 00  |................|
000020  52 00 51 00 5a 00 02 00  00 00 09 00 02 00 00 00  |R.Q.Z...........|
000030  00 00 00 00 00 00 17 00  20 00 86 00 96 00 08 00  |........ .......|
000040  0a 00 09 00 00 00 02 00  02 00 01 00 00 00 1a 00  |................|
000050  02 00 00 00 05 00 00 00  01 00 03 00 00 00 80 00  |................|
000060  00 00 fd 00 00 00 00 00  01 00 00 00 00 00 00 00  |................|
000070  00 00 ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
```

r0 = 3

## Minish Cap

```
000000  8a 00 15 88 02 00 02 00  8a 00 cf bf 02 00 02 00  |................|
000010  8a 00 15 88 02 00 02 00  8a 00 cf bf 02 00 02 00  |................|
000020  52 00 51 00 5a 00 02 00  00 00 09 00 02 00 00 00  |R.Q.Z...........|
000030  00 00 00 00 00 00 17 00  20 00 86 00 96 00 08 00  |........ .......|
000040  0a 00 09 00 00 00 02 00  02 00 01 00 00 00 1a 00  |................|
000050  02 00 00 00 05 00 00 00  01 00 03 00 00 00 80 00  |................|
000060  00 00 fd 00 00 00 00 00  01 00 00 00 00 00 00 00  |................|
000070  00 00 ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
```

r0 = 3

## Pokemon Emerald

no change

# Pattern 2

```
*0x000000 = 0xf0f0
*0x0000aa = 0x9898
```

```
*0x000000 = 0x00f0
*0x0000aa = 0x0098
```

```
*0x000000 = 0x00ff
*0x0000aa = 0x0098
```

## Kingdom Hearts

no change

## Pokemon Emerald

```
000000  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
000010  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
000020  52 00 51 00 5a 00 01 00  00 00 40 00 00 00 00 00  |R.Q.Z.....@.....|
000030  00 00 00 00 00 00 27 00  35 00 00 00 00 00 03 00  |......'.5.......|
000040  05 00 0a 00 13 00 03 00  06 00 03 00 01 00 18 00  |................|
000050  01 00 00 00 05 00 00 00  02 00 7f 00 00 00 00 00  |................|
000060  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000070  00 00 00 00 00 00 00 00  00 00 ff ff ff ff ff ff  |................|
000080  50 00 51 00 4a 00 32 00  33 00 14 00 01 00 02 00  |P.Q.J.2.3.......|
000090  00 00 08 00 00 00 00 00  01 00 96 00 a6 00 04 00  |................|
0000a0  02 00 ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
0000b0  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
0000c0  ff ff ff ff ff ff ff ff  ff ff ff ff 00 00 00 00  |................|
0000d0  ff ff ff ff 00 00 ff ff  ff ff ff ff 00 00 00 00  |................|
0000e0  ff ff ff ff ff ff ff ff  00 00 ff ff 00 00 ff ff  |................|
0000f0  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
```

r0 = 2

# Flash type 3 (Kingdom Hearts, Minish Cap)

Clear sector of 0x8000 bytes:
```
    let sector = 0x0000;

    //// Erase 0x8000 bytes sector

    // Unlock sector
    bus_gba_write(port, sector, 0xff)?;
    bus_gba_write(port, sector, 0x60)?;
    bus_gba_write(port, sector, 0xd0)?;
    bus_gba_write(port, sector, 0x90)?;

    for _ in 0..32 {
        let v = bus_gba_read_word(port, sector + 2)?;
        if v & 0x03 == 0 {
            break;
        }
        thread::sleep(Duration::from_millis(50));
    }

    // Erase sector
    bus_gba_write(port, sector, 0xff)?;
    bus_gba_write(port, sector, 0x20)?;
    bus_gba_write(port, sector, 0xd0)?;

    loop {
        let v = bus_gba_read_word(port, sector)?;
        if v == 0x80 {
            break;
        }
        thread::sleep(Duration::from_millis(50));
    }

    bus_gba_write(port, sector, 0xff)?;
```

Write data (requires unlocked sector):

```
    //// Write data
    let sector = 0x88;

    let data = [0xde, 0xad, 0xbe, 0xef];

    for i in 0..data.len() / 2 {
        let addr = sector + (i * 2) as u32;
        bus_gba_write(port, addr, 0xff)?;
        bus_gba_write(port, addr, 0x70)?;

        loop {
            let v = bus_gba_read_word(port, addr)?;
            if v == 0x80 {
                break;
            }
            thread::sleep(Duration::from_millis(50));
        }

        bus_gba_write(port, addr, 0xff)?;
        bus_gba_write(port, addr, 0x40)?;

        let w = (data[i * 2] as u16) | ((data[i * 2 + 1] as u16) << 8);
        bus_gba_write(port, addr, w)?;

        loop {
            let v = bus_gba_read_word(port, addr)?;
            if v == 0x80 {
                break;
            }
            thread::sleep(Duration::from_millis(50));
        }
    }
    bus_gba_write(port, sector, 0xff)?;
```
