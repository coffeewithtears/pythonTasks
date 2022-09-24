import sys
def decorator_for_UpAndLow(function):
    def wrapper(lint):
        func = function(lint)
        do_swap = lint.swapcase()
        return do_swap
    return wrapper


@decorator_for_UpAndLow
def smth(lint):
    return(lint)

print(smth(input()))