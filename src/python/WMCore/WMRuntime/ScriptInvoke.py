#!/usr/bin/env python
"""
_ScriptInvoker_

Util to invoke a Runtime Script and provide it with access to the
various bits of the job that it will need to access via the WMTaskSpace
library

This script will be invoked at runtime from the directory & subshell
environment in which the Runtime Script implementation needs to be called.


"""

import os
import sys

from WMCore.WMRuntime.ScriptFactory import getScript

class ScriptInvoke:
    """
    _ScriptInvoke_

    Ctor takes two arguments:
    - module name of step module in WMTaskSpace
    - module name of the Script implementation to be invoked

    """
    def __init__(self, stepModule, scriptModule):
        self.step = stepModule
        self.module = scriptModule
        self.exitCode = 0
        self.stepSpace = None
        self.script = None

    def boot(self):
        """
        _boot_

        Import the Step Module & get the stepSpace object from it.
        Get an instance of the Script from the Script Factory

        """
        self.stepSpace = __import__(self.step,
                                    globals(), locals(), ['stepSpace'], -1)
        self.script = getScript(scriptModule)
        self.script.stepSpace = self.stepSpace

    def invoke(self):
        """
        _invoke_

        call the Script implementation

        """
        self.exitCode = self.script()




    def exit(self):
        return self.exitCode


if __name__ == '__main__':

    try:
        stepModule = sys.argv[1]
        scriptModule = sys.argv[2]
    except Exception, ex:
        msg = "Usage: ScriptInvoke.py <Step Module> <Script Module>"
        raise RuntimeError, msg

    invoker = ScriptInvoke(stepModule, scriptModule)

    try:
        invoker.boot()
    except Exception, ex:
        msg = "Error booting script invoker for step %s\n" % stepModule
        msg += "withe Script module: %s\n" % scriptModule
        msg += str(ex)
        raise RuntimeError, msg

    try:
        invoker.invoke()
    except Exception, ex:
        msg = "Error invoking script for step %s\n" % stepModule
        msg += "withe Script module: %s\n" % scriptModule
        msg += str(ex)
        raise RuntimeError, msg

    sys.exit(invoker.exit())



