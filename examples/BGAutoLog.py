from bpdefs import COMMENT, PROPERTIES, ASSIGN, SHOW, LOOP, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Comment for ui: COMMENT(text)
COMMENT("Launch args: duration, interval, units (optional)"),
# Comment for ui: COMMENT(text)
COMMENT(" 'duration' - minutes, unless changed by 'units'"),
# Comment for ui: COMMENT(text)
COMMENT("'interval' - log every ___ seconds"),
# Comment for ui: COMMENT(text)
COMMENT("'units' - (of duration) 'hours', 'minutes', 'seconds'"),
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="False",pause="False"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("duration",
	exp="BP.getArgs().get('duration',100)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("units",
	exp="BP.getArgs().get('units', 'Minutes')"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("interval",
	exp="BP.getArgs().get('interval', 30)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("dur_secs",
	exp="toSecs(duration, units)"),
# Print to run log: SHOW([items=(list of items)] or [string='string_to_print'])
SHOW(string="'Logging every {2} s for {0} {1}'.format(duration,units,interval)"),
# Loop for a duration: LOOP(dur="float" [,units='Seconds' Second|Minutes|Hours ] [,var=''] [,mininc=''])
LOOP(dur="dur_secs",
	units="Seconds",
	var="x",
	mininc="interval",
	steps=(
		# Log a data record: LOG([avg='Default'] [,match='Default'] [,matchH2O='Default'] [,flr='Default'] [flash='Default'])
		LOG(),
	)
),
]
