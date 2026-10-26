
def simulate_dfa(string):
    # Transition table
    transitions = {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q1", "b": "q2"},
        "q2": {"a": "q1", "b": "q0"}
    }

    initial_state = "q0"
    final_states = {"q2"}
    state = initial_state
    path = [state]

    # Process each character
    for symbol in string:
        if symbol not in {"a", "b"}:
            print("Invalid input alphabet")
            return

        state = transitions[state][symbol]
        path.append(state)

    # Display transition path
    print("Transition Path:")
    print(" -> ".join(path))

    # Check acceptance
    if state in final_states:
        print("Accepted")
    else:
        print("Rejected")


# Accept multiple strings
n = int(input("Enter number of strings: "))

for i in range(n):
    string = input("Enter string: ")
    simulate_dfa(string)

