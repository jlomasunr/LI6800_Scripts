from bpdefs import PROPERTIES, TABLE, LOOP, LOG, WAIT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="True",pause="False"),
# Control table: TABLE('name', table, [,dlg=Nothing()])
TABLE("outer_table",
	[('CO2_r', [300, 400, 500, 600])]),
# Control table: TABLE('name', table, [,dlg=Nothing()])
TABLE("inner_table",
	[('Qin', [1500, 1250, 1000, 750, 500, 250, 100]),
		('minWait', [300, 60, '', '', '', '', ''], {'format': ['f', 1, 2], 'units': 'secs'}),
		('maxWait', [500, 120, '', '', '', '', ''], {'format': ['f', 1, 2], 'units': 'secs'}),
		]),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="outer_table",
	var="outer_index",
	steps=(
		# Open a log file: LOG(file=name [,app=False])
		LOG(open="\"/home/licor/logs/co2_\"+str(outer_index)",app=False),
		# Log a remark: LOG(rem=string)
		LOG(rem="'automatic file'"),
		# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
		LOOP(list="inner_table",
			var="inner_index",
			steps=(
				# Wait for statility: WAIT(min="float_seconds", max="float_seconds" [,early=False])]
				WAIT(min="minWait",max="maxWait",early="False"),
				# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
				LOG(avg="On"),
			)
		),
		# Close a log file: LOG(close='')
		LOG(close=0),
	)
),
]
