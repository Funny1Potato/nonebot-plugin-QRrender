from pydantic import BaseModel


class Config(BaseModel):
    """Plugin Config Here"""    
    qr_res:int = 5
