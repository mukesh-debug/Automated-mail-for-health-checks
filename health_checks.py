#!/usr/bin/env python3
import psutil
#more info about psutil at 'https://psutil.readthedocs.io/en/latest/#system-related-functions'
import shutil
#more info about shutil at "https://docs.python.org/3/library/shutil.html"
import dns.resolver

def cpu_usage():
    """Returns False if cpu usage is equal to or over 80%"""
    usage=psutil.cpu_percent(2) #here interval of time as parameter is in seconds
    return usage<0.8

def disk_free():
    """Returns False if disk space available in system partition is less than 20%"""
    t, u, f =shutil.disk_usage('/')
    disk_space=(f/t)
    return disk_space>0.20

def free_memory():
    """Returns False if physical memory available is less than 500 MegaBytes"""
    vm=psutil.virtual_memory()
    return (vm.available/1024**2)>=500

def resolve_host():
    """This function uses dnspython library's function to resolve hostname and check if it is 127.0.0.1 or not.
    Returns False when hostname 'localhost' doesn't resolve to '127.0.0.1'."""
    res=dns.resolver.resolve('localhost', 'A')
    for v in res:
        ip=v.to_text()
    return ip=='127.0.0.1'


def error_identification(cu, du, mu, rh):
    """This function is to identify the error on the system
    It returns a string stating the error identified by the script health_checks.py"""
    sub=""
    if not cu:
        sub+='Error-CPU usage is over 80%'
    if not du:
        sub+='Error-Available disk space is less than 20%'
    if not mu:
        sub+='Error-Available memory is less than 500MB'
    if not rh:
        sub+='Error-localhost cannot be resolved to 127.0.0.1'
    return sub

if __name__=='__main__':
    cpu=cpu_usage()
    disk=disk_free()
    memory=free_memory()
    host_resolve=resolve_host()
    print('cpu usage within limits: ', cpu)
    print('Enough disk space available: ', disk)
    print('Physical memory available is more than or equal to 500 MB : ', memory)
    print('Hostname "localhost" resolves to "127.0.0.1": ', host_resolve)
    print('email subject: ', error_identification(cpu, disk, memory, host_resolve))
