leak016: clean
	./melgen-fusion-186_bdba ow=o i=main-building/leaktestR016.inp
	./melcor-fusion-186_bdba main-building/leaktestR016.inp
leak129: clean
	./melgen-fusion-186_bdba ow=o i=main-building/leaktestR129.inp
	./melcor-fusion-186_bdba main-building/leaktestR129.inp
leak0091: clean
	./melgen-fusion-186_bdba ow=o i=main-building/leaktestR0091.inp
	./melcor-fusion-186_bdba main-building/leaktestR0091.inp
leak0092: clean
	./melgen-fusion-186_bdba ow=o i=main-building/leaktestR0092.inp
	./melcor-fusion-186_bdba main-building/leaktestR0092.inp
l0: clean
	./melgen-fusion-186_bdba ow=o i=L0/l0.inp
	./melcor-fusion-186_bdba L0/l0.inp
l1: clean
	./melgen-fusion-186_bdba ow=o i=L1/l1.inp
	./melcor-fusion-186_bdba L1/l1.inp
mbs: clean
	./melgen-fusion-186_bdba ow=o i=main-building/mbs.inpz
	./melcor-fusion-186_bdba main-building/mbs.inp
sgs: clean
	./melgen-fusion-186_bdba ow=o i=SGS-Ar/sgs.inp
	./melcor-fusion-186_bdba SGS-Ar/sgs.inp
sgs2: clean
	./melgen-fusion-186_bdba ow=o i=SGS-Ar/sgs2.inp
	./melcor-fusion-186_bdba SGS-Ar/sgs2.inp
mb: clean
	./melgen-fusion-186_bdba ow=o i=main-building/main.inp
	./melcor-fusion-186_bdba main-building/main.inp
rhum: clean
	./melgen-fusion-186_bdba ow=o i=main-building/rhum.inp
	./melcor-fusion-186_bdba main-building/rhum.inp
sgs3: clean
	./melgen-fusion-186_bdba ow=o i=SGS-Ar/sgs3.inp
	./melcor-fusion-186_bdba SGS-Ar/sgs3.inp
HLR1: clean
	./melgen-fusion-186_bdba ow=o i=SGS-Ar/NO-INLET/HLR0001.inp
	./melcor-fusion-186_bdba SGS-Ar/NO-INLET/HLR0001.inp
sgsf: clean
	./melgen-fusion-186_bdba ow=o i=SGS-Ar/sgs_final.inp
	./melcor-fusion-186_bdba SGS-Ar/sgs_final.inp
clean:
	rm -f *.DIA
	rm -f *.MES
	rm -f *.OUT
	rm -f *.RST
	rm -f extDIAG
	rm -f MEGDIA
	rm -f MEGOUT
	rm -f MELDIA
	rm -f MELOUT
	rm -f *.dia
	rm -f *.out
	rm -f fort*
cleanall:
	rm -f *.DIA
	rm -f *.MES
	rm -f *.OUT
	rm -f *.PTF
	rm -f *.RST
	rm -f *.DAT
	rm -f extDIAG
	rm -f MEGDIA
	rm -f MEGOUT
	rm -f MELDIA
	rm -f MELOUT
	rm -f *.dia
	rm -f *.out
	rm -f fort*