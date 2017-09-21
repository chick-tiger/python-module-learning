#!/usr/bin/python


####################################################

__version__ = 'CN IDC NXOS Configuration Automation'
__author__ = 'Chengjie Liu'
__contact__ = 'cjliu@blizzard.com'

####################################################




import warnings
with warnings.catch_warnings(record=True) as w:
    import paramiko

import multiprocessing
from datetime import datetime

import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

import argparse

from CN_IDC_DEVICES import HGH2_MS, HGH2_BL, HGH2_SS, HGH2_CTRL_PLANE, HGH2A_HL_UCS, HGH2B_HL_UCS, HGH2A_HL_DELL, HGH2B_HL_DELL, HGH2_HL_DELL_HYPER, HGH2A_HL_VIVOX, HGH2B_HL_VIVOX, HGH2_TS_KAFKA_REGIONAL, HGH2_TS_CASSANDRA, HGH2_TS_ELASTICSEARCH, HGH2_TS_FLUKE, HGH2_TS_EXDATA, HGH2_TS_N5K_PTR, HGH2_TS_N5K_ADMIN, HGH2_BARE_METAL, HGH3_MS, HGH3_BL, HGH3_SS, HGH3_CTRL_PLANE, HGH3A_HL_UCS, HGH3B_HL_UCS, HGH3A_HL_DELL, HGH3B_HL_DELL, HGH3_HL_DELL_HYPER, HGH3_TS_DATABASE, HGH3_TS_FLUKE, HGH3_TS_EXDATA, HGH3_TS_N5K_ADMIN, HGH3_BARE_METAL

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='NXOS Configuration Automation - \
Import Configuration from flat text file and define the device type')

parser.add_argument('-i',help='Configuration Input File - Example: /home/user/rfc1234.txt - #### Be Sure to end your Input file with commmit and/or wr mem depending on device type #####',required=True)
parser.add_argument('-d',help='Device type: ', type=str.upper, required=True)

args = parser.parse_args()


if args.d == 'HGH2_MS':
    devices = HGH2_MS
elif args.d == 'HGH2_BL':
    devices = HGH2_BL
elif args.d == 'HGH2_SS':
    devices = HGH2_SS
elif args.d == 'HGH2_CTRL_PLANE':
    devices = HGH2_CTRL_PLANE
elif args.d == 'HGH2A_HL_UCS':
    devices = HGH2A_HL_UCS
elif args.d == 'HGH2B_HL_UCS':
    devices = HGH2B_HL_UCS
elif args.d == 'HGH2A_HL_DELL':
    devices = HGH2A_HL_DELL
elif args.d == 'HGH2B_HL_DELL':
    devices = HGH2B_HL_DELL
elif args.d == 'HGH2_HL_DELL_HYPER':
    devices = HGH2_HL_DELL_HYPER
elif args.d == 'HGH2A_HL_VIVOX':
    devices = HGH2A_HL_VIVOX
elif args.d == 'HGH2B_HL_VIVOX':
    devices = HGH2B_HL_VIVOX
elif args.d == 'HGH2_TS_KAFKA_REGIONAL':
    devices = HGH2_TS_KAFKA_REGIONAL
elif args.d == 'HGH2_TS_CASSANDRA':
    devices = HGH2_TS_CASSANDRA
elif args.d == 'HGH2_TS_ELASTICSEARCH':
    devices = HGH2_TS_ELASTICSEARCH
elif args.d == 'HGH2_TS_FLUKE':
    devices = HGH2_TS_FLUKE
elif args.d == 'HGH2_TS_EXDATA':
    devices = HGH2_TS_EXDATA
elif args.d == 'HGH2_TS_N5K_PTR':
    devices = HGH2_TS_N5K_PTR
elif args.d == 'HGH2_TS_N5K_ADMIN':
    devices = HGH2_TS_N5K_ADMIN
elif args.d == 'HGH2_BARE_METAL':
    devices = HGH2_BARE_METAL
elif args.d == 'HGH3_MS':
    devices = HGH3_MS
elif args.d == 'HGH3_BL':
    devices = HGH3_BL
elif args.d == 'HGH3_SS':
    devices = HGH3_SS
elif args.d == 'HGH3_CTRL_PLANE':
    devices = HGH3_CTRL_PLANE
elif args.d == 'HGH3A_HL_UCS':
    devices = HGH3A_HL_UCS
elif args.d == 'HGH3B_HL_UCS':
    devices = HGH3B_HL_UCS
elif args.d == 'HGH3A_HL_DELL':
    devices = HGH3A_HL_DELL
elif args.d == 'HGH3B_HL_DELL':
    devices = HGH3B_HL_DELL
elif args.d == 'HGH3_HL_DELL_HYPER':
    devices = HGH3_HL_DELL_HYPER
elif args.d == 'HGH3A_HL_VIVOX':
    devices = HGH3A_HL_VIVOX
elif args.d == 'HGH3_TS_DATABASE':
    devices = HGH3_TS_DATABASE
elif args.d == 'HGH3_TS_FLUKE':
    devices = HGH3_TS_FLUKE
elif args.d == 'HGH3_TS_EXDATA':
    devices = HGH3_TS_EXDATA
elif args.d == 'HGH3_TS_N5K_ADMIN':
    devices = HGH3_TS_N5K_ADMIN
elif args.d == 'HGH3_BARE_METAL':
    devices = HGH3_BARE_METAL
else:
    print 'Please enter a valid device type'

config = open(args.i).read().splitlines()


def print_output(results):

    print "\nSuccessful devices:"
    for a_dict in results:
        for identifier,v in a_dict.iteritems():
            (success, out_string) = v
            if success:
                print '\n\n'
                print '#' * 80
                print 'Device = {0}\n'.format(identifier)
                print out_string
                print '#' * 80

    print "\n\nFailed devices:\n"
    for a_dict in results:
        for identifier,v in a_dict.iteritems():
            (success, out_string) = v
            if not success:
                print 'Device failed = {0}'.format(identifier)

    print "\nEnd time: " + str(datetime.now())
    print


def worker_config_cmds(a_device, mp_queue):
    '''
    Return a dictionary where the key is the device identifier
    Value is (success|fail(boolean), return_string)
    '''
    try:
        a_device['port']
    except KeyError:
        a_device['port'] = 22

    identifier = '{ip}:{port}'.format(**a_device)
    return_data = {}

    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])

    try:
        net_connect = SSHClass(**a_device)
        config_cmds = net_connect.send_config_set(config,delay_factor=.3)
        print "configuration pushed to: " + a_device["ip"]
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier] = (False, e)

        # Add data to the queue (for parent process)
        mp_queue.put(return_data)
        return None

    return_data[identifier] = (True, config_cmds)
    mp_queue.put(return_data)

def main():

    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time: " + str(datetime.now())

    for a_device in devices:

        p = multiprocessing.Process(target=worker_config_cmds, args=(a_device, mp_queue))
        processes.append(p)
        # start the work process
        p.start()

    # wait until the child processes have completed
    for p in processes:
        p.join()

    # retrieve all the data from the queue
    results = []
    for p in processes:
        results.append(mp_queue.get())

    print_output(results)


if __name__ == '__main__':

    main()
