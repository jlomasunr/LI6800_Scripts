from bpdefs import ASSIGN, LOOP, SETCONTROL, LOG, Nothing, CheckBox,Text, Button, DropDown, RadioBtns, EditBox
steps=[
SETCONTROL("VDP_leaf","1.8","float"),
SETCONTROL("t_leaf", "23", "float"),

LOOP(dur="1441",
    units="Minutes",
    mininc="300"
    steps=(
        LOG(),
        # When the lights go off, update the temperature and humidity settings
        IF("Qin<10",
            steps=(
                SETCONTROL("VDP_leaf","1.2","float"),
                LOG(rem="VDP_leaf updated to 1.2 based on Qin")
                )
            ),
        IF("Qin<10",
            steps=(
                SETCONTROL("t_leaf","21","float"),
                LOG(rem="t_leaf updated to 21C based on Qin")
                )
            ),
        # When the lights come on, update the temperature and humidity settings
        IF("Qin>=10",
            steps=(
                SETCONTROL("VDP_leaf","1.8","float"),
                LOG(rem="VDP_leaf updated to 1.8 based on Qin")
                )
            ),
        IF("Qin>=10",
            steps=(
                SETCONTROL("t_leaf","23","float"),
                LOG(rem="t_leaf updated to 23C based on Qin")
                )
            ),

    ))]
