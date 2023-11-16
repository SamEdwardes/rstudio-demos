from __future__ import annotations

import json
from typing import Annotated

from fastapi import FastAPI, Request, Header, Depends
from pydantic import BaseModel, Field
app = FastAPI()


class UserMetadata(BaseModel):
    user: str
    groups: list[str] = Field(list)

    @classmethod
    def from_header_string(cls, rstudio_connect_credentials: str) -> UserMetadata:
        # Convert the header string to a dict.
        json_data = json.loads(rstudio_connect_credentials)
        # Convert the dict to a `UserMetadata` object.
        user_meta_data = cls(**json_data)
        return user_meta_data


@app.get("/whoami")
async def get_whoami(request: Request) -> UserMetadata:
    """
    Headers can be obtained using the `Request` object.
    """ 
    rstudio_connect_credentials = request.headers.get("rstudio-connect-credentials")
    user_meta_data = UserMetadata.from_header_string(rstudio_connect_credentials)
    return UserMetadata(**user_meta_data)


@app.get("/whoami2")
async def get_whoami2(rstudio_connect_credentials: Annotated[str | None, Header()] = None) -> UserMetadata:
    """
    Headers can be obtained using the `Header` object directly.
    """
    user_meta_data = UserMetadata.from_header_string(rstudio_connect_credentials)
    return user_meta_data


async def get_current_user(rstudio_connect_credentials: Annotated[str | None, Header()] = None):
    """
    FastAPI also had a dependency injection system that can be used.
    """
    user_meta_data = UserMetadata.from_header_string(rstudio_connect_credentials)
    return user_meta_data


@app.get("/whoami3")
async def get_whoami3(user = Depends(get_current_user)) -> UserMetadata:
    """
    Rely on the depedency injection system for getting the user metadata.
    """
    return user
