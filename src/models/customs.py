from typing import Annotated

from pydantic import StringConstraints

Extension = Annotated[str, StringConstraints(pattern=r"\.*")]
