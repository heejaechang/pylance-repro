 # SCENARIO: `Add "./outsideLib" to extraPaths` should work in a multiroot workspace
 # TARGET: `outerModule` in `import outerModule`
 # TRIGGER: open `test.code-workspace`, use the lightbulb on `outerModule`, and choose `Add "./outsideLib" to extraPaths`
 # EXPECT: the import issue resolves or the workspace settings gain the matching `extraPaths` entry
 # VERIFY: if the import stays broken and `test.code-workspace` is unchanged, the bug still reproduces
 # RECOVER: remove the added `extraPaths` entry from `test.code-workspace`

import outerModule
