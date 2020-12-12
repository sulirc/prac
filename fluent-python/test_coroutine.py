def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

my_coro = simple_coroutine()
# my_coro.send(1999)
my_coro.send(None)
print(my_coro)
next(my_coro)
my_coro.send(42)

