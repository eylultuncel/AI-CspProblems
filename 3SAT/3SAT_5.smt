(set-logic QF_UF)
(set-option :produce-models true)
(declare-const E Bool)
(declare-const Y Bool)
(declare-const L Bool)
(declare-const U Bool)
(declare-const T Bool)
(declare-const N Bool)
(declare-const C Bool)
(assert
	(and
		(or E Y L )
		(or L U L )
		(or T U N )
		(or C E L )
		(or (not E) (not Y) L )
		(or (not L) (not U) L )
		(or (not T) (not U) N )
		(or (not C) (not E) L )	
	) 
)
(check-sat)
(get-model)
(exit)
