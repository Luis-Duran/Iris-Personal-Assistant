"""Functions Relatrd to Desktop/OS Operations"""
import os

appDictionary = {'spotify' : 'spotify.exe',
                 'chrome' : '\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"'}
def openApp(app):
    os.system(appDictionary[app])
