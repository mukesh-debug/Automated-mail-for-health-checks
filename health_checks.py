#!/usr/bin/env python3
import psutil
#more info about psutil at 'https://psutil.readthedocs.io/en/latest/#system-related-functions'
import shutil
#more info about shutil at "https://docs.python.org/3/library/shutil.html"

def cpu_usage():
    """Returns False if cpu usage is equal to or over 80%"""
    usage=psutil.cpu_percent(1)
    return usage<0.8:

def disk_free():
    """Returns False if disk space available in system partition is less than 20%"""
    t, u, f =shutil.disk_usage('/')
    disk_space=(f/t)
    return disk_space>0.20

def free_memory():
    """Returns false if physical memory available is less than 500 MegaBytes"""
    vm=psutil.virtual_memory()
    return (vm.available/1024**2)>500
