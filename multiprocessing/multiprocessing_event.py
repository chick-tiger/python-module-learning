import multiprocessing
import time

def wait_for_event(e):
    print 'waiting for event: starting '
    e.wait()
    print 'waiting for event: is event set ? >> ', e.is_set()

def wait_for_event_timeout(e, t):
    print 'waiting for event timeout: starting '
    e.wait(t)
    print 'waiting for event: is event set ? >> ', e.is_set()


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e,))
    w1.start()


    w2 = multiprocessing.Process(name='non-block', target=wait_for_event_timeout, args=(e,2))
    w2.start()

    print 'main: waiting before calling Event.set()'
    time.sleep(3)
    e.set()
    print 'main: event is set'
