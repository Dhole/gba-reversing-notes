# Chinese bootleg ROM dumps hashes

| File Name                          | sha256 |
|------------------------------------|--------|
| `chinese_12_in_1.gba`              | `aac75449e8ee992e38acc1e5fc4a2d70a0b40cc02d6df2febebfbb0c3bcb2b7b` |
| `chinese_kingdom_hearts.gba`       | `03301734073b05b6943016e6c87658b14b4e1bea1d56452efd430a03c0f5c171` | 
| `chinese_pokemon_emerald.gba`      | `5d183a0c489bba704b987e3601aeb80050efae6ff2f48c082b07b33576e4294b` |
| `chinese_pokemon_ruby.gba`         | `02ba52ac8cf025f90ca8861e27a38ba1411d412fec4acb253adf2b62afd083d2` |
| `chinese_zelda_minish_cap_16M.gba` | `da28546c4b189b8054ee91b2613ceb7f882229c652b5be4dcfa4054d43e58af9` |
| `chinese_zelda_minish_cap.gba`     | `d8d65326300b014aff2bdf2da4907e56b2fbc09db758eb2cf7a17da00c948e67` |

# Original ROM dump hashes used for comparison

| ROM Name                                | sha256 |
|-----------------------------------------|--------|
| Zelda - the Minish Cap                  | `c84645731952b7677f514ae222683504066334ab2af904e64a8a84ffc1af46c6`|
| Kingdom Hearts - Chain of Memories      | `6f6e7b61bb7b6ef7e2bea6e9dd01e70570a715835cc3713abe86186fd2c4e28d`|
| Pokemon - Emerald Version (USA, Europe) | `a9dec84dfe7f62ab2220bafaef7479da0929d066ece16a6885f6226db19085af`|
| Pokemon - Ruby Version (USA)            | `53d591215de2cab847d14fbcf8c516f0128cfa8556f1236065e0535aa5936d4e`|

# Obtaining bootleg dump from the patch:

First find the original ROM with the hash matching that listed in the previous section.

The patches have been made using the bsdiff tool.  To get the bootleg dump do:
```
bspatch original_rom.gba chinese_bootleg_rom.gba chinese_bootleg_rom.gba.bspatch
```
