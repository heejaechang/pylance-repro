 # SCENARIO: going to stdlib definitions should not flood Problems with library diagnostics
 # TARGET: `join` in `os.path.join('a', 'b')`
 # TRIGGER: run go to definition on `join`
 # EXPECT: navigation works without adding stdlib diagnostics to the workspace Problems view
 # VERIFY: if the Problems count jumps after entering the stdlib file, the bug still reproduces
 # RECOVER: return to the workspace file or close the library tab

import os


os.path.join('a', 'b')