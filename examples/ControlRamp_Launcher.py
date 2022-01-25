from bpdefs import EXEC, SHOW, WHILE, COMMENT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Include the module
EXEC(0,file="/home/licor/resources/lib/thread_examples.py"),
# Make an instance of ControlRmp, call it xxx
EXEC(0,source="xxx=ControlRamp('CO2_r', 300, 1000, 60)"),
# Launch the thread. (Using BP.launch() makes the xxx thread a dependent)
EXEC(0,source="BP.launch(xxx)"),
# Wait while the thread is running
WHILE("xxx.is_alive()",
	mininc="1",
	steps=(
		# Comment for ui: COMMENT(text)
		COMMENT("<Insert steps here>"),
	)
),
]
