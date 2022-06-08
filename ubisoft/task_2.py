import time


def retry(tries: int = -1, delay=0):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            cnt = tries
            while cnt:
                func(*args, **kwargs)
                cnt -= 1
                if not cnt:
                    break
                time.sleep(delay)
        return wrapped
    return wrapper


@retry(tries=3)
def foo(num):
    print(f'foo {num}')


if __name__ == '__main__':
    foo('haha')
