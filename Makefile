leak: clean
	./melgen-fusion-186_bdba L0/leaktest.inp
	./melcor-fusion-186_bdba L0/leaktest.inp
l0: clean
	./melgen-fusion-186_bdba L0/l0.inp
	./melcor-fusion-186_bdba L0/l0.inp
l1: clean
	./melgen-fusion-186_bdba L1/l1.inp
	./melcor-fusion-186_bdba L1/l1.inp
clean:
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