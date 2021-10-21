(set-logic QF_UF)
(set-option :produce-models true)
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(declare-const E Bool)
(assert
	(=>
		(and A B C D )
            	E
	) 
)
(check-sat)
(get-model)
(exit)
