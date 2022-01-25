from bpdefs import GROUP, ASSIGN, CALL, SHOW, EXEC, DEFINE, WAIT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Collection: GROUP(enabled, label)
GROUP("True","WaitForFlashCaptureValues",
	steps=(
		# ff_name will eventually hold the flr event file name 
		ASSIGN("ff_name",
			exp="''"),
		# Make a flash (1=rect). numbers defined below.
		CALL("FlashAndWait",
			['1', 'ff_name']),
		# Show the file name of the flr event that just happened
		SHOW(items="ff_name"),
		# Open the file, convert to a python structure (dict)
		EXEC(0,source="event_data = json.load(open(ff_name, 'r'))"),
		# Pick off two things from the file and show them
		SHOW(string="'FMax = {0}, Qmax={1}'.format(event_data['FMAX'], event_data['QMAX'])"),
		# This subroutine will do a flr event, wait for it to be done, and return the event file name.
	)
),
]
