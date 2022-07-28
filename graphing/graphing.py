from typing import Any, Union
from graphing.env import *
from _utils.valtype import Query, validate_instance, default_validate_instance, PathLike

class Viz:
    def __init__(self) -> None:
        pass
    
    def add_instrument(self, instrument: Query) -> None:
        validate_instance(instrument, Query)
        
    def graph(self, __io: PathLike) -> None:
        validate_instance(__io, PathLike)
        
        