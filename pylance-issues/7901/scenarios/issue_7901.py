# SCENARIO: TypedDict key completion should expose value-type information in the completion UI
# TARGET: the empty key position inside `takes_config({"": 0})`
# TRIGGER: trigger completion between the quotes
# EXPECT: completion rows would show the key and its associated value type information
# VERIFY: if rows still show only key names, the enhancement remains unimplemented

from typing import TypedDict


class Config(TypedDict):
    cli_path: str
    log_level: int
    use_stdio: bool


def takes_config(config: Config) -> None:
    pass


takes_config({"": 0})