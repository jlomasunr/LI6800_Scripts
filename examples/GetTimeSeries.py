from bpdefs import ASSIGN, EXEC, LOOP, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("f",
	exp="open('/home/licor/logs/light_series.txt','w')"),
# Assign a variable to a Data Dictionary entry: ASSIGN('varname', dd=DataDict('group', 'name' [,bool_logged]) [,track=False] [,optvar='varname'] [dlg=Nothing()))])
ASSIGN("q",
	dd=DataDict('PPFD_out','Meas'),
	track=True),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="print(\"Time,Light\",file=f)"),
# Loop for a duration: LOOP(dur="float" [,units='Seconds' Second|Minutes|Hours ] [,var=''] [,mininc=''])
LOOP(dur="1",
	units="Hours",
	mininc="2",
	steps=(
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("hhmmss",
			exp="datetime.now().strftime(\"%H:%M:%S\")"),
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("line",
			exp="'{0},{1}'.format(hhmmss,q)"),
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="print(line,file=f)"),
	)
),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="f.close()"),
]
