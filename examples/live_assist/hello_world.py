#! /usr/local/bin/python3
# Hello world example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v57.0+.

from cefpython3 import cefpython as cef
import platform
import sys

live_room = "http://live.dz11.com/77595203"

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    browser = cef.CreateBrowserSync(url=live_room, window_title="Hello World!")
    set_client_handles(browser)
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


def set_client_handles(browser):
    browser.SetClientHandler(EventHandler())


class EventHandler(object):

    def OnLoadingStateChange(self, browser, is_loading, **_):
        if is_loading:
            print('loading...')
        else:
            print('loading completed')
            line = open('alert.js').read()
            browser.ExecuteJavascript(line)

if __name__ == '__main__':
    main()
