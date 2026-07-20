dfa = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
final_state = "q2"
user_input = input("Enter a string to test: ")
strings = [user_input]
try:
    count = int(user_input)
    strings = []
    for _ in range(count):
        strings.append(input("Enter String: "))
except ValueError:
    pass
for string in strings:
    state = "q0"
    path = [state]
    valid = True
    for ch in string:
        if ch not in ['a', 'b']:
            valid = False
            break
        state = dfa[state][ch]
        path.append(state)
    print("Transition Path:")
    print(" -> ".join(path))
    if valid and state == final_state:
        print("Accepted")
    else:
        print("Rejected")