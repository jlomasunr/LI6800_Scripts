from bpdefs import EXEC, GROUP, ASSIGN, LOOP, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox, DataDict

steps=[
# We will use BPTable and BPGraph, defined in bpoutput.py
EXEC(0,file="/home/licor/resources/lib/bpoutput.py"),
# 
GROUP("True","Define output table",
	steps=(
		# Create a table
		EXEC(0,source="table=BPTable()"),
		# Set the title of the banner
		EXEC(0,source="table.setTopLabel(\"Final Stats\")"),
		# This table will have two fixed rows. We add columns as we get them
		EXEC(0,source="table.define(rows=['Mean', 'Stdev'])"),
	)
),
# 
GROUP("True","Setup Graph",
	steps=(
		# Create a graph
		ASSIGN("xyg",
			exp="BPGraph()"),
		# Set the title of the top banner
		EXEC(0,source="xyg.setTopLabel('Realtime Graph')"),
		# clear the graph
		EXEC(0,source="xyg.clear()"),
		# Set the graph title
		EXEC(0,source="xyg.setTitle('Live Data + Running Mean')"),
		# Label the axes
		EXEC(0,source="xyg.labelAxes(xbottom='Elapsed (s)',yleft='CO2_r')"),
		# Define a plot series. Save the series id in variable ds. We'll use it to add data to this series
		EXEC(0,source="ds = xyg.plotLeft([],[],symbol='+',line='-')"),
		# Define the mean marker. Save the id as variable ms. We'll need to move the marker around as the mean changes. 
		EXEC(0,source="ms = xyg.markLineLeft(0, line='--', text='Mean', color='grey', align='^>')"),
		# Show the graph
		EXEC(0,source="xyg.show()"),
	)
),
# 
GROUP("True","Collect and plot data",
	steps=(
		# co2 will track CO2_r
		ASSIGN("co2",
			dd=DataDict('CO2_r','Meas'),
			track=True),
		# To get stats, we'll collect values in a list named data
		ASSIGN("data",
			exp="[]"),
		# For 30 seconds, whenever new readings are available....
		LOOP(dur="30",
			units="Seconds",
			var="t",
			mininc="0",
			steps=(
				# Plot co2 by updating the data series named ds
				EXEC(0,source="xyg.addData(ds, t, co2)"),
				# Append to the data list
				EXEC(0,source="data.append(co2)"),
				# Move the marker to show where the mean is now
				EXEC(0,source="xyg.modMarker(ms, yleft=sum(data)/len(data))"),
			)
		),
	)
),
# When done, we update the table
GROUP("True","Show Stats in Table",
	steps=(
		# Convert data to a numpy array, to make stddev computation easy
		EXEC(0,source="npa=np.array(data)"),
		# Add a column named CO2_r to the table with two values (one for each row)
		EXEC(0,source="table.add('CO2_r', [npa.mean(), npa.std()])"),
	)
),
]
