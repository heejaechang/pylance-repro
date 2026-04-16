 # SCENARIO: the type-checking status item should update when `pyrightconfig.json` changes
 # TARGET: the status-bar type-checking mode while this folder is open
 # TRIGGER: edit and save `pyrightconfig.json`, flipping `typeCheckingMode`
 # EXPECT: the status bar updates without a window reload
 # VERIFY: if the status bar changes only after reloading the window, the bug still reproduces
 # RECOVER: restore `pyrightconfig.json` or reload the window

x = 1