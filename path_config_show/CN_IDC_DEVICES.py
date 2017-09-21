##################################

__version__ = 'CN IDC NXOS devices'
__author__ = 'Chengjie Liu'
__contact__ = 'cjliu@blizzard.com'

##################################


username = 'test'
password = 'test'


def nxos(device):
    return {
        'username': username,
        'password': password,
        'device_type': 'cisco_nxos',
        'ip': device,
    }
def iosxr(device):
    return {
        'username': username,
        'password': password,
        'device_type': 'cisco_xr',
        'ip': device,
    }
TPE1_HL = [
    nxos('hl01-r12rb-hitpe1.network.cloud.blizzard.net'),
    nxos('hl02-r12rb-hitpe1.network.cloud.blizzard.net'),
    nxos('hl01-r13ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl01-r14ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl02-r13ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl02-r14ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl01-r16ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl01-r17ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl02-r16ri-hitpe1.network.cloud.blizzard.net'),
    nxos('hl02-r17ri-hitpe1.network.cloud.blizzard.net'),
]

"""

def ios(device):
    return {
        'username': username,
        'password': password,
        'device_type': 'cisco_ios',
        'ip': device,
    }


def junos(device):
    return {
        'username': username,
        'password': password,
        'device_type': 'juniper',
        'ip': device,
    }

def acos(device):
    return {
        'username': username,
        'password': password,
        'device_type': 'a10',
        'ip': device,
        'global_delay_factor': 5,
    }

"""
