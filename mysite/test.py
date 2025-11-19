from typing import Any, Callable

type data = dict[str, Any]
type exportFn = Callable[[data], Any]

exporters: dict[str, exportFn] = {}