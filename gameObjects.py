THINGS = ""
room = ""
ROOMNAME = ""
ZONENAME = ""
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
Up = "up", "north", "n"
Down = "down", "south", "s"
Left = "left", "west", "w"
Right = "right", "east", "e"
Door = "d", "door", "enter"

items = {
    "pen": {
       DESCRIPTION: "a nice pen",
        },
}

rooms = {
    'b2': {
        DESCRIPTION: "blah blah blah",
        THINGS: items["pen"][DESCRIPTION]

    }
}

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: "Busy area of town, You spot two exits, one to the south and one to the east",
        EXAMINATION: "There are a few decent looking shops here. It's too bad you have no coin to spend",
        SOLVED: False,
        Down: "b1",
        Right: "a2",
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION:'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Down: "b2",
        Left: "a1",
        Right: "a3",
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Down: "b3",
        Left: "a2",
        Right: "a4",
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Down: "b4",
        Left: "a3",
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a1",
        Down: "c1",
        Right: "b2",
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This is your Home!',
        EXAMINATION: "It hasn't changed since the last time you looked...",
        SOLVED: False,
        Up: "a2",
        Down: "c2",
        Left: "b1",
        room: rooms["b2"]

    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a3",
        Down: "c3",
        Left: "b2",
        Right:"b4",
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: "a4",
        Down: "c4",
        Left: "b3",
    },
}
