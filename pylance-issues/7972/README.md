# Issue #7972: variable type inlay hints seem to be truncated to 32 characters, regardless of the editor inline hint length setting

- Source: https://github.com/microsoft/pylance-release/issues/7972
- State: open
- Created: 2026-04-07T12:28:56+00:00
- Updated: 2026-04-07T12:41:01+00:00
- Labels: team needs to reproduce, ai-triage-responded

## Reporter context

## Environment data

<!--
To find your version, open the VS Code extensions panel, then locate Pylance from the list of installed extensions. The version appears next to the name.
-->

-   Pylance version: 2026.2.1
-  VS Code: 1.114.0
-   OS and version: Win 11 (26100.7985)
_-   Python version (& distribution if applicable, e.g. Anaconda): CPython 3.13 and 3.14_

## Code Snippet

```python
from collections.abc import Iterable
from types import MappingProxyType

def t():
    d : dict[str, Iterable[int]] = {}
    return MappingProxyType(d)

v = t()
```

## Repro Steps

- Copy code snippet.
- make sure, Variable Type inlay hints are enabled
- _(optional, for comparison: make sure, Function Return Types inlay hints are enabled as well)_


You can really see this, when you set `vscode://settings/editor.inlayHints.maximumLength` to 29 and the increase it in increments of 1:
- `29`: everything looks right  
   (both values are truncated and this is shown with what looks like the ellipsis unicode char)
   <img width="341" height="120" alt="Image" src="https://github.com/user-attachments/assets/6fe7b4aa-fbba-4883-9e45-cfbc4d73634b" />


- `30` - `31`:  
   the function inlay hint grows longer as expected, but in the variable type inlay hint, only two dots appear instead of the expected letters  
   <img width="380" height="125" alt="Image" src="https://github.com/user-attachments/assets/ce6553c6-1d02-415f-aefd-973880e00fba" />
   with the setting at 31, you can see the difference between the first two dots, which are just dot-characters and the last 3 dots, which are a single character


-   `32` and bigger :   
   the variable type inlay hint stops growing, while the function type inlay hint expands until it is fully visible:  
   <img width="430" height="119" alt="Image" src="https://github.com/user-attachments/assets/b8f88059-b7bf-4d29-942c-c14a1203c1d5" />  



## Expected behavior

I expect the variable type inlay hints to behave like the function return type inlay hints:

They should get truncated according to the `editor.inlayHints.maximumLength`-Setting.

## Actual behavior
The variable type inlay hints are truncated after 32 characters, regardless of the setting:

<img width="428" height="25" alt="Image" src="https://github.com/user-attachments/assets/ccfd2e58-75f3-464c-80c8-376809247e4e" />

<img width="355" height="29" alt="Image" src="https://github.com/user-attachments/assets/37fc9499-158f-4719-bf6a-0fe9db92298b" />


To me, it looks like pylance is performing it's own truncation before handing over the inlay hint to the vs code editor, which is actually supposed to perform the truncation according to the limit from the settings


## beyond this bugreport

it could be a nice feature to be able to set different length limits for different inlay hint types

e.g. variable type inlay hints appear earlier in a line of code, so one might want to keep them short and be able to see the rest of the line, while function return type inlay hints appear toward the end of a line, so one might prefer to allow them to be longer and be able to read the entire hint, even if the line continues past the normal limits

similarly, one might value the extra verbosity in pytest parameters, but want to keep other inlay hints short to preserve code readability.

but i guess that would require the vs code editor to support different types of inlay hints (or maybe tags for inlay hints), so it's probably not worth the overall effort and added complexity
