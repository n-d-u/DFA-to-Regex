import json

# states = input("Enter States\n").split()
# letters = input("Enter letters\n").split()
# tf = input("TF\n").split()
# tf2 = [[]*3]*len(tf)
#
# for i in range(len(tf2)):
#     tf2[i] = tf[i].split(":")
#
# startStates = input("Enter Start States\n").split()
# finalStates = input("Enter Final States\n").split()
# x = {
#     "states": states,
#     "letters": letters,
#     "transition_function": tf2,
#     "transition_matrix": tf2,
#     "start_states": startStates,
#     "final_states": finalStates
# }
#
# y = json.dumps(x)
# with open("sample.json", "w") as outfile:
#     outfile.write(y)


def w2json(states, letters, tf2, startStates, finalStates):
    x = {
        "states": states,
        "letters": letters,
        "transition_function": tf2,
        # "transition_matrix": tf2,
        "start_states": startStates,
        "final_states": finalStates
    }
    y = json.dumps(x)
    with open("static/json/inputMain.json", "w") as outfile:
        outfile.write(y)