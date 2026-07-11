"""
Simulates the airflow module structure for issue #7998.
conf is a module-level object imported from another module.
"""


class _Conf:
    def getboolean(self, section: str, option: str, *, fallback: bool) -> bool:
        return fallback


conf = _Conf()


class FileSensor:
    def __init__(
        self,
        *,
        filepath,
        fs_conn_id="fs_default",
        recursive=False,
        deferrable: bool = conf.getboolean("operators", "default_deferrable", fallback=False),
        **kwargs,
    ):
        pass
