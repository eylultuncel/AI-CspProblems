(set-logic QF_UF)
(set-option :produce-models true)
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(assert
	(and
		(or A B )
		(or B C )
		(or C D )
		(or D A )
		(or A C )
		(or B (not C) )
		(or C (not D) )
		(or D B )	
	) 
)
(check-sat)
(get-model)
(exit)


