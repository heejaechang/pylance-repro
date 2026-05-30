from typing import overload, Any


class Point3d:
    x: float
    y: float
    z: float


class ObjectId:
    pass


class OpenMode:
    pass


class Curve:
    def __init__(self) -> None:
        """Curve base class constructor."""


class Line(Curve):
    @overload
    def __init__(self, /) -> None: ...
    @overload
    def __init__(self, start: Point3d, end: Point3d, /) -> None: ...
    @overload
    def __init__(self, id: ObjectId, /) -> None: ...
    @overload
    def __init__(self, id: ObjectId, mode: OpenMode, /) -> None: ...
    @overload
    def __init__(self, id: ObjectId, mode: OpenMode, erased: bool, /) -> None: ...
    @overload
    def __init__(self, *args) -> None:
        """
        The AcDbLine class represents the line entity in AutoCAD. A line object is a 3D object that
        is specified by its start point, endpoint, and normal vector. In addition, the line object
        supports thickness along its normal vector direction (that is, height or "extrusion").
        """
    def __reduce__(self, /) -> Any: ...
