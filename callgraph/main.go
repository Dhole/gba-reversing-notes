package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	ROMStart   = 0x8000000
	ROMEnd     = 0xa000000
	BIOSStart  = 0x0000000
	BIOSEnd    = 0x0004000
	IWRAMStart = 0x3000000
	IWRAMEnd   = 0x3008000
)

type Region string

const (
	RegionROM   Region = "ROM"
	RegionBIOS  Region = "BIOS"
	RegionIWRAM Region = "IWRAM"
)

func GetRegion(addr uint32) Region {
	if addr >= ROMStart && addr < ROMEnd {
		return RegionROM
	} else if addr >= BIOSStart && addr < BIOSEnd {
		return RegionBIOS
	} else if addr >= IWRAMStart && addr < IWRAMEnd {
		return RegionIWRAM
	} else {
		return Region("Unknown")
	}
}

type Op string

const (
	OpBx Op = "bx"
	OpBl Op = "bl"
	OpUn Op = "??"
)

type Mode byte

const (
	ModeARM     Mode = 'A'
	ModeThumb   Mode = 'T'
	ModeUnknown Mode = '?'
)

type Jump struct {
	SrcMode, DstMode Mode
	Src, Dst         uint32
	Op               Op
	FnAddr           uint32
}

type AddressJumps struct {
	In  *Jump
	Out *Jump
}

type JumpList struct {
	Addresses []AddressJumps
}

func NewJumpList() JumpList {
	return JumpList{
		Addresses: make([]AddressJumps, (ROMEnd-ROMStart)/2),
	}
}

func (jl *JumpList) AddIn(addr uint32, jump *Jump) {
	addr -= ROMStart
	jl.Addresses[addr/2].In = jump
}

func (jl *JumpList) GetIn(addr uint32) *Jump {
	addr -= ROMStart
	return jl.Addresses[addr/2].In
}

func (jl *JumpList) AddOut(addr uint32, jump *Jump) {
	addr -= ROMStart
	jl.Addresses[addr/2].Out = jump
}

func (jl *JumpList) GetOut(addr uint32) *Jump {
	addr -= ROMStart
	return jl.Addresses[addr/2].Out
}

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	defer f.Close()
	jl := NewJumpList()
	fmt.Println("Parsing log...")
	var lineNum int
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		var jump Jump
		line := sc.Text()
		if _, err := fmt.Sscanf(line, "%c 0x%x %s %c 0x%x\n",
			&jump.SrcMode, &jump.Src, &jump.Op, &jump.DstMode, &jump.Dst); err != nil {
			fmt.Printf("Error in line %v: %v : %v\n", lineNum, line, err)
			continue
		}
		if jump.Op == OpBl {
			// if jump.Dst == 0x080b0c0c {
			// 	fmt.Printf("A) %#v\n", jump)
			// }
			if GetRegion(jump.Src) == RegionROM {
				jl.AddOut(jump.Src, &jump)
			}
			if GetRegion(jump.Dst) == RegionROM {
				jl.AddIn(jump.Dst, &jump)
			}
		} else {
			if GetRegion(jump.Src) == RegionROM {
				jl.AddOut(jump.Src, &jump)
			}
		}
		lineNum++
		// fmt.Printf("%02d: %c 0x%08x %s %c 0x%08x\n",
		// 	i, jump.SrcMode, jump.Src, jump.Op, jump.DstMode, jump.Dst)
	}
	fmt.Println("Parsing log finished!")
	var inFn bool
	var fnAddr uint32
	for i := 0; i < len(jl.Addresses); i++ {
		aj := jl.Addresses[i]
		// if i*2+ROMStart == 0x080b0c0c {
		// 	fmt.Printf("B) %#v\n", aj)
		// }
		if !inFn {
			if aj.In != nil && aj.In.Op == OpBl {
				// Function begin
				// fmt.Printf("0x%08x - ", aj.In.Dst)
				inFn = true
				fnAddr = aj.In.Dst
				// fmt.Printf("0x%08x\n", fnAddr)
				i--
			}
		} else {
			if aj.Out != nil && aj.Out.Op != OpBl {
				// Function end
				// fmt.Printf("0x%08x\n", aj.Out.Src)
				inFn = false
			}
		}
		if inFn && aj.Out != nil && aj.Out.Op == OpBl {
			aj.Out.FnAddr = fnAddr
		}
	}

	for _, aj := range jl.Addresses {
		if aj.Out != nil && aj.Out.Op == OpBl {
			fmt.Printf("\"0x%08x\" -> \"0x%08x\"\n", aj.Out.FnAddr, aj.Out.Dst)
		}
	}
}
