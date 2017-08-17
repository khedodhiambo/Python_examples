# One thing to be very aware of with Python is that default values are created at def
# time, therefore, subsequent calls to the same function will possibly behave differently
# according to the mutability of their default values


def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 50)

    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one
func()
func()
func()
func()
func()
func()
func()
func()
func()
func()
