leak016: clean
	./melgen-fusion-186_bdba Main Building/leaktestR016.inp
	./melcor-fusion-186_bdba Main Building/leaktestR016.inp
leak129: clean
	./melgen-fusion-186_bdba Main Building/leaktestR129.inp
	./melcor-fusion-186_bdba Main Building/leaktestR129.inp
leak0091: clean
	./melgen-fusion-186_bdba Main Building/leaktestR0091.inp
	./melcor-fusion-186_bdba Main Building/leaktestR0091.inp
leak0092: clean
	./melgen-fusion-186_bdba Main Building/leaktestR0092.inp
	./melcor-fusion-186_bdba Main Building/leaktestR0092.inp
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
sgs2: clean
	./melgen-fusion-186_bdba Main Building/sgs2.inp
	./melcor-fusion-186_bdba Main Building/sgs2.inp
mb: clean
	./melgen-fusion-186_bdba Main Building/main.inp
	./melcor-fusion-186_bdba  Main Building/main.inp
rhum: clean
	./melgen-fusion-186_bdba Main Building/rhum.inp
	./melcor-fusion-186_bdba  Main Building/rhum.inp
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