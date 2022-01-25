from bpdefs import IF, RETURN, ASSIGN, LOOP, EXEC, SHOW, DIALOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("elist",
	exp="[]"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("title",
	exp="BP.getArgs().get('title', 'Dynamic Dialog')"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("subtitle",
	exp="BP.getArgs().get('subtitle', '')"),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="BP.getArgs().get('items', [])",
	var="x",
	steps=(
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="BP.registerThis(x, False)"),
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="elist.append('{0}'.format(x))"),
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="BP.registerThis(x+'_dlg', {'target':x, 'interface': 1, 'label': 'Take a '+x})"),
	)
),
# Open a dialog: DIALOG(title=string [,sub=string] [,text=string] [,items=list_of_edit_items] [,buttons=list_of_buttons] [var=pressed_btn_name])
DIALOG(title="title",
	sub="subtitle",
	items="elist",
	buttons="['Cancel','OK']",
	var="button"),
IF("button == 'OK'",
	steps=(
		# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
		ASSIGN("result",
			exp="{}"),
		# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
		LOOP(list="elist",
			var="x",
			steps=(
				# Compile and run python: EXEC(scope, [source=code] or [file=filename])
				EXEC(0,source="result[x] = BP.varValue(x)"),
			)
		),
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="BP.setResult(result)"),
	)
),
]
