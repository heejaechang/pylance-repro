 # SCENARIO: auto-indent should dedent nested `else` blocks correctly
 # TARGET: the outer `else:` that follows the nested block
 # TRIGGER: press Enter after the inner block and type the outer `else:`
 # EXPECT: the outer `else:` dedents to match the first `if`
 # VERIFY: if the outer `else:` stays indented under the inner block, the bug still reproduces
 # RECOVER: no recovery needed

if foo:
    if bar:
        print('bar')
    else:
        print('foo')