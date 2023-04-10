leak: clean
	./melgen-fusion-186_bdba Main Building/leaktest.inp
	./melcor-fusion-186_bdba Main Building/leaktest.inp
l0: clean
	./melgen-fusion-186_bdba L0/l0.inp
	./melcor-fusion-186_bdba L0/l0.inp
l1: clean
	./melgen-fusion-186_bdba L1/l1.inp
	./melcor-fusion-186_bdba L1/l1.inp
mbs: clean
	./melgen-fusion-186_bdba Main Building/mbs.inp
	./melcor-fusion-186_bdba Main Building/mbs.inp
sgs: clean
	./melgen-fusion-186_bdba Main Building/sgs.inp
	./melcor-fusion-186_bdba Main Building/sgs.inp
mb: clean
	./melgen-fusion-186_bdba Main Building/main.inp
	./melcor-fusion-186_bdba  Main Building/main.inp
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
	rm -f extDIAG
	rm -f MEGDIA
	rm -f MEGOUT
	rm -f MELDIA
	rm -f MELOUT
	rm -f *.dia
	rm -f *.out
	rm -f fort*