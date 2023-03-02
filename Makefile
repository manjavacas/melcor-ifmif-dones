leak: clean
	./melgen-fusion-186_bdba L0/leaktest.inp
	./melcor-fusion-186_bdba L0/leaktest.inp
l0: clean
	./melgen-fusion-186_bdba L0/l0.inp
	./melcor-fusion-186_bdba L0/l0.inp
l1: clean
	./melgen-fusion-186_bdba L1/l1.inp
	./melcor-fusion-186_bdba L1/l1.inp
l0s: clean
	./melgen-fusion-186_bdba L0/l0_simpl.inp
	./melcor-fusion-186_bdba L0/l0_simpl.inp
l1s: clean
	./melgen-fusion-186_bdba L1/l1_simpl.inp
	./melcor-fusion-186_bdba L1/l1_simpl.inp
mb: clean
	./melgen-fusion-186_bdba Main Building/main.inp
	./melcor-fusion-186_bdba  Main Building/main.inp
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