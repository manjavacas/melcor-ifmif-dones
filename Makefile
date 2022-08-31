all: clean gen cor

foo: clean
	./melgen-fusion-186_bdba L0v2.inp
	./melcor-fusion-186_bdba L0v2.cor
gen: clean
	./melgen-fusion-186_bdba L0.inp
cor:
	./melcor-fusion-186_bdba L0.cor 
clean:
	rm -f *.OUT
	rm -f *.out
	rm -f *.PTF
	rm -f *.RST
	rm -f *.DIA
	rm -f *.MES
	rm -f *.dia
	rm -f extDIAG