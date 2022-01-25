from bpdefs import GROUP, COMMENT, ASSIGN, EXEC, LOOP, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Collection: GROUP(enabled, label)
GROUP("True","Time examples",
	steps=(
		# Comment for ui: COMMENT(text)
		COMMENT("Useful functions"),
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("fct_now",
			exp="lambda : datetime.now()"),
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("fct_elapsed",
			exp="lambda x:(datetime.now() - x).total_seconds()"),
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("fct_hr",
			exp="lambda x: x.hour+x.minute/60.0+x.second/3600."),
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("fct_hms",
			exp="lambda x: x.strftime(\"%H:%M:%S\")"),
	)
),
# Assign a variable to a topic/key item: ASSIGN('varname', topic='topic_name' [,key=''] [,track=False] [,dlg=Nothing()])
ASSIGN("meas",
	topic="'Meas'",
	track=True),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("f",
	exp="open('/home/licor/logs/mydata_meas.txt', 'w')"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("labels",
	exp="sorted(list(meas.keys()))"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="print('Elapsed',',',str(labels)[1:-1], file=f)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("start",
	exp="fct_now()"),
# Loop for a duration: LOOP(dur="float" [,units='Seconds' Second|Minutes|Hours ] [,var=''] [,mininc=''])
LOOP(dur="10",
	units="Seconds",
	mininc="0",
	steps=(
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("line",
			exp="str([meas[i] for i in labels])[1:-1]"),
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="print(fct_elapsed(start),',',line, file=f)"),
	)
),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="f.close()"),
]
