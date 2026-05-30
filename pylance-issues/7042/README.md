# Issue #7042 - Move symbol to doesn't work if the sub directory has a hyphen in it

**Issue**: https://github.com/microsoft/pylance-release/issues/7042

## Workspace Structure

```
hyphen-dir/
  source.py   - Contains a function to move
  target.py   - Target file for the move
```

## Repro Steps (from issue)

1. Create a subdirectory in your open folder with a hyphen in it, like 'hyphen-dir'
2. Create two files in the subdirectory
3. Create a function in one of the files
4. Refactor -> Move Symbol To .. on the function
5. Move it to the other file

## Expected behavior

> "It works"

## Actual behavior

The move symbol refactoring silently fails (no code action available or action does nothing).

## Verification Checklist

- [ ] Open this workspace in VS Code with Pylance
- [ ] Open `hyphen-dir/source.py`
- [ ] Place cursor on `my_function`
- [ ] Invoke Refactor -> Move Symbol To...
- [ ] Select `hyphen-dir/target.py` as destination
- [ ] Verify whether the move succeeds or fails silently
