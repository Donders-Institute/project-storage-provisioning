#!/bin/env python
import sys
import os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../external/lib/python')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '../')
from utils.Common   import getConfig, getMyLogger
from utils.IStorage import StorageType, createProjectDirectory

## load configuration file
cfg  = getConfig( os.path.dirname(os.path.abspath(__file__)) + '/etc/config.ini' )

fpath = '/project/0000000.03'
quota = '%sGB' % '300'
stype = 'netapp_volume'

logger = getMyLogger(lvl=3)

rc = createProjectDirectory(fpath, quota, StorageType[stype], cfg, lvl=3)

if rc:
    # must refresh the PROJECT_BASEDIR to get access to the newly created volume 
    os.listdir(cfg.get('PPS','PROJECT_BASEDIR'))
    if not os.path.exists( fpath ):
        logger.error('created directory not available: %s' % fpath)
