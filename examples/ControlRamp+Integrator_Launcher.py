from bpdefs import EXEC, LOOP, WAIT, ASSIGN, SHOW, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,file="/home/licor/resources/lib/thread_examples.py"),
# Make a ControlRamp for light
EXEC(0,source="ct=ControlRamp('Qin',100, 1000, 300)"),
# Make an Integrator for light
EXEC(0,source="itg=Integrator('Qin', 'licor/li6850/scripts/leafq/data')"),
# Start both as dependents
EXEC(0,source="BP.launch(itg);BP.launch(ct)"),
# Loop two times
LOOP(count="2",
	steps=(
		# Reset the Integrator
		EXEC(0,source="itg.reset()"),
		# Loop 3 times
		LOOP(count="3",
			steps=(
				# Wait a bit
				WAIT(dur="10",units="Seconds"),
				# Get the Integrator's output
				ASSIGN("f",
					exp="itg.getstatus()"),
				# Print Integrator's results so far
				SHOW(string="'After {0:1.1f}s, mean={1:1.1f}, integ={2:1.1f}'.format(f['elapsed'], f['average'],f['integrated'])"),
			)
		),
	)
),
]
