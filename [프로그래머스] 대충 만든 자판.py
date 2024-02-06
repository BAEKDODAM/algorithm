def solution(keymap, targets):
    keytable = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)

    result = []
    for target in targets:
        clicked = 0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked += keytable[key]
        result.append(clicked)

    return result
