#!/usr/bin/env python3

import sys
import r2pipe

_SRAM_PATCHES = {
    'EEPROM_V124': [
        (
            'a2b00d1c0004030c0348006880888342'
            '05d3014848e0',
            '00040a1c400be0210905411807310023'
            '08781070013301320139072bf8d90020'
            '70bc02bc0847'),
        (
            'f0b5acb00d1c0004010c1206170e0348'
            '00688088814205d3',
            '70b500040a1c400be021090541180731'
            '002310780870013301320139072bf8d9'
            '002070bc02bc0847'),
        ],
    'EEPROM_V120': [
        (
            'a2b00d1c0004030c0348006880888342'
            '05d3014848e0',
            '00040a1c400be0210905411807310023'
            '08781070013301320139072bf8d90020'
            '70bc02bc0847'),
        (
            '30b5a9b00d1c0004040c034800688088'
            '844205d3014859e0',
            '70b500040a1c400be021090541180731'
            '002310780870013301320139072bf8d9'
            '002070bc02bc0847'),
        ],
    }

SRAM_PATCHES = {
        # 'FLASH1M_V102': [],
        # 'FLASH1M_V103': [],
        # 'FLASH_v120': [],
        # 'FLASH_v121': [],
        # 'FLASH_v123': [],
        # 'FLASH_v124': [],
        # 'FLASH_v125': [],
        # 'FLASH_v126': [],
        # 'FLASH512_V130': [],
        # 'FLASH512_V131': [],
        # 'FLASH512_V133': [],
        # 'EEPROM_V111': [],
        'EEPROM_V120': _SRAM_PATCHES['EEPROM_V120'],
        'EEPROM_V121': _SRAM_PATCHES['EEPROM_V120'],
        'EEPROM_V122': _SRAM_PATCHES['EEPROM_V120'],
        'EEPROM_V124': _SRAM_PATCHES['EEPROM_V124'],
        # 'EEPROM_V126': [],
        }
EEPROM_V120_V112_0 = 'a2b00d1c0004030c034800688088834205d30148..e0'

filename = sys.argv[1]

r2 = r2pipe.open(filename)


for storage in ['EEPROM_V', 'SRAM_V', 'FLASH_V', 'FLASH512_V', 'FLASH1M_V']:
    print(f'Searching for {storage}nnn')
    res = r2.cmdj(f'/j {storage}')
    if len(res) > 0:
        print(res)
        offset = res[0]["offset"]
        print(hex(offset), ':', r2.cmd(f'ps @ {offset}'), end="")
        break

# res = r2.cmdj(f'/xj {EEPROM_V120_V112_0}')
# print('---')
# print(res)