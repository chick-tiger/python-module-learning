#!/usr/bin/python
import multiprocessing
import time
import sys

def daemon():
	print 'Starting', multiprocessing.current_process().name
	time.sleep(3)
	print 'Exiting', multiprocessing.current_process().name

def non_daemon():
	print 'Starting', multiprocessing.current_process().name
	print 'Exiting', multiprocessing.current_process().name

if __name__ == "__main__":
	d = multiprocessing.Process(name='daemon', target=daemon)
	d.daemon = True

	n = multiprocessing.Process(name='non_daemon', target=non_daemon)
	n.daemon = False

	d.start()
	n.start()
	
	d.join(1)
	print 'd.is_alive()', d.is_alive()
	n.join()