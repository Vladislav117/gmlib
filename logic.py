class Gate:
    def __init__(self, state=False):
        self._state = bool(state)

    def state(self):
        return self._state

    def switch(self):
        self._state = not self._state
        return self

    def off(self):
        self._state = False
        return self

    def on(self):
        self._state = True
        return self

    def set(self, state: bool):
        self._state = bool(state)
        return self

    def switchIF(self, condition: bool):
        if condition:
            self._state = not self._state
        return self

    def offIF(self, condition: bool):
        if condition:
            self._state = False
        return self

    def onIF(self, condition: bool):
        if condition:
            self._state = True
        return self

    def setIF(self, state: bool, condition: bool):
        if condition:
            self._state = bool(state)
        return self

    def __bool__(self):
        return self._state

    def __int__(self):
        return int(self._state)

    def __float__(self):
        return float(self._state)

    def __str__(self):
        return str(self._state)

    def __repr__(self):
        return f' -> {self._state} -> '


def andMany(*values):
    result = True
    for value in values:
        print('o')
        if not value:
            result = False
            break
        result = result and value
    return result


def orMany(*values):
    result = False
    for value in values:
        if value:
            result = True
            break
        result = result or value
    return result


def notMany(*values):
    result = list(values)
    for value_index in range(len(result)):
        result[value_index] = not result[value_index]
    return result
