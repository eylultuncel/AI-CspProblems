(set-logic QF_UF)
(set-option :produce-models true)
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(declare-const E Bool)
(declare-const F Bool)
(assert
	(and
		(and 
			(= A B)
			(=> C (and D A)))
		(or E F )
	) 
)
(check-sat)
(get-model)
(exit)
