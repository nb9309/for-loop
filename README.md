# for-loop

2. for loop  or   for ...else  loop

Syntax1:-

			for varname  in  Iterable_object:
				  ----------------------------------------
				  Indentation block of stmts
				  ----------------------------------------
			    ---------------------------------------------------
			Other statements in Program
			---------------------------------------------------
		
---------------
Syntax2:

			for varname in Iterable_object:
				  ----------------------------------------
				  Indentation block of stmts
				  ----------------------------------------
			else:
				  ----------------------------------------
				  else block of statements
				  ----------------------------------------
			    ---------------------------------------------------
			Other statements in Program
			---------------------------------------------------

Explanation:
-----------------------
=>Here 'for' , "in" and 'else' are keywords
=>Here Iterable_object can be Sequence(bytes,bytearray,range,str), 
    list(list,tuple),set(set,frozenset) and dict.
=>The execution process of for loop is that " Each of Element of Iterable_object selected , placed in varname and executes Indentation block of statements".This Process will be repeated until all elements of Iterable_object completed.
=> when all the elements of Iterable Object completed  then PVM  comes out of for loop and executes else block of statements which are written under else block 
=>Writing else block is optional.
