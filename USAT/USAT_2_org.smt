(set-logic QF_UF)
(set-option :produce-models true)
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(assert
	(=>
		(and A B )
		(=> 
			(=> (not B) C) 
			A )
	) 
)
(check-sat)
(get-model)
(exit)
