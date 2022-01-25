from bpdefs import EXEC, GROUP, ASSIGN, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox, DataDict

steps=[
# Load the bpoutput library file
EXEC(0,file="/home/licor/resources/lib/bpoutput.py"),
# Collection: GROUP(enabled, label)
GROUP("True","Graph",
	steps=(
		# xyg is our instance of the class for plotting
		ASSIGN("xyg",
			exp="BPGraph()"),
		# x is a list of values 
		ASSIGN("x",
			exp="[1,2,3,4,5,6]"),
		# z is those values cubed
		ASSIGN("z",
			exp="[i*i*i for i in x]"),
		# y is those values squared
		ASSIGN("y",
			exp="[i*i for i in x]"),
		# y1 is squared divided by 2
		ASSIGN("y1",
			exp="[i*i/2 for i in x]"),
		# Start with a clear graph
		EXEC(0,source="xyg.clear()"),
		# Label the bottom, left, and right aces
		EXEC(0,source="xyg.labelAxes(xbottom='X value',yleft='Y value',yright='Z value')"),
		# plot x vs y on the left. Everything defaulted, put series into 'squared' legend group
		EXEC(0,source="xyg.plotLeft(x,y,legend='squared')"),
		# Also plot x, y1 on the left. Specify dashed line instead of points.
		EXEC(0,source="xyg.plotLeft(x,y1,legend='squared', line='--')"),
		# Plot x, z on the right. Points and a solid line, specify colors and sizes.
		EXEC(0,source="xyg.plotRight(x,z,legend='cubed',symbol='o', size=10, color='aqua', line='-')"),
		# Put up the title
		EXEC(0,source="xyg.setTitle('BP Demo Graph')"),
		# show the graph
		EXEC(0,source="xyg.show()"),
	)
),
]
