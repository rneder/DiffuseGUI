from lib_discus_suite import *
#
#  Maintains a status as to where the GUI is
#
#  STATUS =  0   ! in   SUITE
#  STATUS =  1   ! in   DISCUS
#  STATUS = -1   ! in a DISCUS submenu
#  STATUS =  2   ! in   KUPLOT
#  STATUS = -2   ! in a KUPLOT submenu
#  STATUS =  3   ! in   DIFFEV
#  STATUS = -3   ! in a DIFFEV submenu


class suite_status:
    STATUS = 0
    def __init__(self, status):
        suite_status.STATUS = 0
        suite_status.INITIAL = -1
        self.set(status)

    def set(self, status):
        suite_status.STATUS = status

    def get(self):
        return suite_status.STATUS

    def change(eff=None, new=0):
        if suite_status.STATUS == 0:  # We were in SUITE, just go to section
            if abs(new) == 1:             # Switch to DISCUS
                line = 'discus'
            elif abs(new) == 2:           # Switch to KUPLOT
                line = 'kuplot'
            elif abs(new) == 3:           # Switch to DIFFEV
                line = 'diffev'
            suite.suite_learn(line)
            suite_status.STATUS = new     # Store current status
        elif suite_status.STATUS == 1:    # We were in DISCUS
            if abs(new) == 0:             # Need to exit DISCUS
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
            elif abs(new) == 2:           # Need to exit DISCUS go to KUPLOT
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'kuplot'
                suite.suite_learn(line)
            elif abs(new) == 3:           # Need to exit DISCUS go to DIFFEV
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'diffev'
                suite.suite_learn(line)
            suite_status.STATUS = new     # Store current status
        elif suite_status.STATUS == 2:    # We were in KUPLOT
            if abs(new) == 0:             # Need to exit KUPLOT
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
            elif abs(new) == 1:           # Need to exit KUPLOT go to DISCUS
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'discus'
                suite.suite_learn(line)
            elif abs(new) == 3:           # Need to exit KUPLOT go to DIFFEV
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'diffev'
                suite.suite_learn(line)
            suite_status.STATUS = new     # Store current status
        elif suite_status.STATUS == 3:    # We were in DIFFEV
            if abs(new) == 0:             # Need to exit DIFFEV
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
            elif abs(new) == 1:           # Need to exit DIFFEV go to DISCUS
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'discus'
                suite.suite_learn(line)
            elif abs(new) == 2:           # Need to exit DIFFEV go to KUPLOT
                line = 'exit'             # go back to SUITE
                suite.suite_learn(line)
                line = 'kuplot'
                suite.suite_learn(line)
            suite_status.STATUS = new     # Store current status

#       if suite_status.STATUS > 0:   # We were in DISCUS KUPLOT OR DIFFEV
#           line = 'exit'             # go back to SUITE
#           suite.suite_learn(line)
#       elif suite_status.STATUS < 0: # We were in SUBMENU of DISCUS KUPLOT OR DIFFEV
#           line = 'exit'             # go back to main menu of the section
#           suite.suite_learn(line)
#           line = 'exit'             # go back to SUITE
#           suite.suite_learn(line)
#       if abs(new) == 1:             # Switch to DISCUS
#           line = 'discus'
#       elif abs(new) == 2:           # Switch to KUPLOT
#           line = 'kuplot'
#       elif abs(new) == 3:           # Switch to DIFFEV
#           line = 'diffev'
#       suite.suite_learn(line)
#       suite_status.STATUS = new     # Store current status


    def nbc(eff=None, parent=None):
        if suite_status.INITIAL == 0:
            tbbs = parent.nb.tabs()
            old = suite_status.STATUS
            if parent.nb.select() == tbbs[0]:   # Activated DISCUS Notebook
                if suite_status.STATUS == 2 or suite_status.STATUS == 3:
                    #                             We were in DISCUS or KUPLOT
                    line = 'exit'             #   go back to SUITE
                    suite.suite_learn(line)
                elif suite_status.STATUS == -2 or suite_status.STATUS == -3:
                    #                             We were in DISCUS or KUPLOT
                    line = 'exit'             #   go back to main menu of section
                    suite.suite_learn(line)
                    line = 'exit'             #   go back to SUITE
                    suite.suite_learn(line)
                line = 'discus'
                suite.suite_learn(line)
                suite_status.STATUS = 1  # Store current status
            elif parent.nb.select() == tbbs[1]:   # Activated KUPLOT Notebook
                if suite_status.STATUS == 1 or suite_status.STATUS == 3:
                    # We were in DISCUS OR DIFFEV
                    line = 'exit'             # go back to SUITE
                    suite.suite_learn(line)
                elif suite_status.STATUS == -1 or suite_status.STATUS == -3:
                    # We were in DISCUS OR DIFFEV
                    line = 'exit'             # go back to main menu of section
                    suite.suite_learn(line)
                    line = 'exit'             # go back to SUITE
                    suite.suite_learn(line)
                line = 'kuplot'
                suite.suite_learn(line)
                suite_status.STATUS = 2  # Store current status
            elif parent.nb.select() == tbbs[2]:    # Activated DIFFEV Notebook
                if suite_status.STATUS == 1 or suite_status.STATUS == 2:
                    # We were in DISCUS KUPLOT
                    line = 'exit'             # go back to SUITE
                    suite.suite_learn(line)
                elif suite_status.STATUS == -1 or suite_status.STATUS == -2:
                    # We were in submenu of DISCUS or KUPLOT
                    line = 'exit'             # go back to main menu of section
                    suite.suite_learn(line)
                    line = 'exit'             # go back to SUITE
                    suite.suite_learn(line)
                line = 'diffev'
                suite.suite_learn(line)
                suite_status.STATUS = 3  # Store current status
        else:
            suite_status.INITIAL = 0
            suite_status.STATUS  = 0
