# SCENARIO: deleting an accidentally committed auto-import completion should also remove the inserted import statement
# TARGET: the standalone `o` below
# TRIGGER: Completion, commit `os`, then delete the committed `os` token immediately without using Undo
# EXPECT: the completion list offers `os` as an auto-import completion and committing it inserts `import os`
# VERIFY: after deleting the committed `os` token, the auto-added `import os` line is removed as well instead of remaining as a dangling import
# RECOVER: revert the file to its original text after the check

o