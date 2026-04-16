# SCENARIO: invoking Quick Fix on an undefined function call should reveal the current generate-symbol surface
# TARGET: `DoSomething`
# TRIGGER: open Quick Fix on the undefined call
# EXPECT: if only Copilot-backed generation is available, the menu shows `Generate function "DoSomething" with Copilot`
# VERIFY: the issue remains valid if there is no built-in typed stub generator comparable to the C# experience
# RECOVER: no recovery needed

result: float = DoSomething(3, 'hello', False)