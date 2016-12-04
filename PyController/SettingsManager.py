#!/usr/bin/env python
# -*- coding=utf-8 -*-

# Author: Ryan Henrichson
# Version: 0.1
# Date: 12/01/2016
# Description: This package loads the configuration files.


import logging
import yaml


mainConfigFile = "main.yaml"
deviceDir = "devices.d/"
profileDir = "profiles.d/"


# logging.basicConfig(format='%(module)s %(funcName)s %(lineno)s %(message)s', level=logging.DEBUG)
log = logging.getLogger('ConfigLoader')


class SettingsManager(object):

    mainConfig = None

    def __init__(self):
        super(SettingsManager, self).__init__()
        self.loadMainConfig()

    def loadMainConfig(self):
        log.info("Loading main config file: %s" % mainConfigFile)
        self.mainConfig = self.loadConfig(mainConfigFile)

    def loadConfig(self, filepath, loadYaml=True, device=False, profile=False):
        if device:
            filepath = self.deviceDir + filepath
        elif profile:
            filepath = self.profileDir + filepath
        with file(filepath) as f:
            config = f.read()
        if loadYaml:
            return yaml.load(config)
        return config

    @property
    def devices(self):
        if not self.mainConfig:
            return []
        return self.mainConfig.get('devices', []) or []

    @property
    def profiles(self):
        if not self.mainConfig:
            return []
        return self.mainConfig.get('profiles', []) or []

    @property
    def deviceDir(self):
        try:
            return self.mainConfig['main']['devicesDir']
        except Exception:
            return deviceDir

    @property
    def profileDir(self):
        try:
            return self.mainConfig['main']['profileDir']
        except Exception:
            return profileDir

    @property
    def logging(self):
        try:
            return self.mainConfig['main']['logging']
        except Exception:
            return False

    @property
    def loggingLevel(self):
        try:
            return self.mainConfig['main']['loglevel']
        except Exception:
            return 'ERROR'

    @property
    def logFile(self):
        try:
            return self.mainConfig['main']['logFile']
        except Exception:
            return ''