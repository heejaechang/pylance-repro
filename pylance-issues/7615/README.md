# Issue #7615: Pylance is extremely slow with 'transformers' package

- **Issue**: https://github.com/microsoft/pylance-release/issues/7615
- **Type**: Performance bug
- **Reporter**: @Guillaume-Lombardo
- **Confirmed by**: @rchiodo, @heejaechang

## Root Cause (confirmed via code inspection)

`_lookUpImport()` in `program.ts:1936-1945` calls `_handleMemoryHighUsage()` before every `_bindFile()` during the binding cascade. For packages with >750 files (transformers has ~38K via wildcard imports), this triggers eviction → re-binding → eviction thrashing loop.

The type-checking path was fixed (PR #3256 with `pauseTracking()` at line ~2104), but the binding path was missed.

## Reproduction

From rchiodo's comment (2026-01-27):

```python
import transformers
processor = transformers.Qwen3VLProcessor.from_pretrained("Qwen/Qwen3-VL-4B-Instruct")

model = transformers.Qwen3VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-VL-4B-Instruct", dtype="auto", device_map="auto"
)
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

inputs = processor.apply_chat_template(
    messages
)
print(f"inputs: {inputs}")
```

## Setup

1. Create a venv: `python -m venv .venv`
2. Install: `pip install transformers torch`
3. Open this folder in VS Code with Pylance

## Verification Checklist

1. Open `test_transformers.py` in the editor
2. **Expected (from issue)**: Analysis takes 10-20 seconds (binding cascade thrashing)
3. **Fixed behavior**: Analysis should complete in <2 seconds
4. Monitor the Pylance output channel for:
   - `Long operation: binding: .../transformers/models/__init__.py`
   - Repeated binding events on the same files (thrashing indicator)

## Notes

- The `transformers` package must be the real package from PyPI (not a stub)
- The issue is about the binding cascade triggered by wildcard imports under `TYPE_CHECKING`
- Latest transformers versions have reduced wildcard imports somewhat, but `from .models import *` still exists
- PR microsoft/pyrx#8077 is open but not merged
- Existing plan: `.github/plans/future/FIX_7615_TRANSFORMERS_SLOW_BINDING_PLAN.md`
