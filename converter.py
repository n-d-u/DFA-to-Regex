import json
from copy import deepcopy
import sys


def calinout(intermediate_states, dfa):
    cart = []
    for x in range(len(intermediate_states)):
        ie = 0
        oe = 0
        for j in range(len(dfa["transition_function"])):
            if dfa["transition_function"][j][2] == intermediate_states[x]:
                ie += 1
            elif dfa["transition_function"][j][0] == intermediate_states[x]:
                oe += 1
        cart.append([intermediate_states[x], (ie, oe)])
    cart.sort(key=lambda a: a[1][0] + a[1][1])
    ie = 0
    oe = 0
    return cart


def get_all_transitions(x_t, dfa):
    outgoing = []
    selfloop = []
    cart = []
    incoming = []

    for x in range(len(dfa["transition_function"])):
        if x_t in dfa["transition_function"][x]:
            cart.append(dfa["transition_function"][x])

    for x in range(len(cart)):
        if x_t == cart[x][0] and x_t != cart[x][2]:
            outgoing.append(cart[x])
        elif x_t == cart[x][2] and x_t != cart[x][0]:
            incoming.append(cart[x])
        else:
            selfloop.append(cart[x])
    return incoming, outgoing, selfloop


def clearOldTransitions(reg, dfa):
    # global dfa
    for x in range(len(reg)):
        if reg[x] in dfa["transition_function"]:
            dfa["transition_function"].remove(reg[x])


def Convertor():
    f = open("static/json/inputMain.json", "r")
    dfa = json.load(f)

    if len(dfa["final_states"]) > 1:
        for x in range(len(dfa["final_states"])):
            idx = len(dfa["transition_function"])
            val = [dfa["final_states"][x], '$', 'Qf']
            dfa["transition_function"].insert(idx, val)

        dfa["final_states"] = ["Qf"]

    start_state = dfa["start_states"][0]
    for x in range(len(dfa["transition_function"])):
        if start_state == dfa["transition_function"][x][2]:
            idx = len(dfa["transition_function"])
            val = ["Qi", "$", start_state]
            dfa["transition_function"].insert(idx, val)
            start_state = "Qi"
            dfa["start_states"][0] = "Qi"
            break

    final_state = dfa["final_states"][0]
    for x in range(len(dfa["transition_function"])):
        if final_state == dfa["transition_function"][x][0]:
            idx = len(dfa["transition_function"])
            val = [final_state, "$", "Qf"]
            dfa["transition_function"].insert(idx, val)
            dfa["final_states"] = ["Qf"]
            break

    intermediate_states = deepcopy(dfa["states"])
    check1 = dfa['start_states'][0]
    if check1 in intermediate_states:
        intermediate_states.remove(check1)
    check2 = dfa['final_states'][0]
    if check2 in intermediate_states:
        intermediate_states.remove(check2)
    ie_edges = calinout(intermediate_states,dfa)
    size_intermediate = len(intermediate_states)

    size_transition = len(dfa["transition_function"])
    while size_transition != 1 and size_intermediate > 0:
        exp = []
        state_to_remove = ie_edges[0][0]
        inc, out, self_loops = get_all_transitions(state_to_remove, dfa)

        if len(self_loops) > 1:
            exp = []
            for lo in range(len(self_loops)):
                idx = len(exp)
                val = self_loops[lo][1]
                exp.insert(idx, val)
                idx = len(exp)
                exp.insert(idx, '+')
            idx = len(exp) - 1
            exp.pop(idx)
            exp = ''.join(exp)

        if len(self_loops) == 1:
            exp = self_loops[0][1]
        if len(self_loops) < 1:
            exp = ''
        for x in range(len(inc)):
            for y in range(len(out)):
                if exp == "":
                    idx = len(dfa["transition_function"])
                    val = [inc[x][0], "{}{}".format(inc[x][1], out[y][1]), out[y][2]]
                    dfa["transition_function"].insert(idx, val)
                elif len(exp) == 1:
                    idx = len(dfa["transition_function"])
                    val = [inc[x][0], "{}{}*{}".format(inc[x][1], exp, out[y][1]), out[y][2]]
                    dfa["transition_function"].insert(idx, val)
                else:
                    idx = len(dfa["transition_function"])
                    val = [inc[x][0], "{}({})*{}".format(inc[x][1], exp, out[y][1]), out[y][2]]
                    dfa["transition_function"].insert(idx, val)

        for x in range(len(out)):
            if out[x] in dfa["transition_function"]:
                dfa["transition_function"].remove(out[x])
        for x in range(len(inc)):
            if inc[x] in dfa["transition_function"]:
                dfa["transition_function"].remove(inc[x])
        for x in range(len(self_loops)):
            if self_loops[x] in dfa["transition_function"]:
                dfa["transition_function"].remove(self_loops[x])

        intermediate_states.remove(state_to_remove)
        ie_edges = calinout(intermediate_states,dfa)
        # ie_edges.sort(key=lambda a:a[1][0]+a[1][1])
        size_intermediate = len(intermediate_states)
        size_transition = len(dfa["transition_function"])

    fg = []
    finalregex = []

    for x in range(len(dfa["transition_function"])):
        idx = len(fg)
        val = dfa["transition_function"][x][1]
        fg.insert(idx, val)
        fg.insert(len(fg), '+')

    if len(fg) > 0:
        idx = len(fg) - 1
        fg.pop(idx)
    fg = ''.join(fg)
    fromm = dfa["transition_function"][0][0]
    to = dfa["transition_function"][0][2]
    dfa["transition_function"] = [[fromm, fg, to]]

    for x in range(len(dfa["transition_function"][0][1])):
        if dfa["transition_function"][0][1][x] != '$':
            finalregex.append(dfa["transition_function"][0][1][x])
    regex = {}
    regex['regex'] = ''.join(finalregex)
    g = open("static/json/outputMain.json", 'w')

    json.dump(regex, g)
