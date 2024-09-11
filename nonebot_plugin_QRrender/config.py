from pydantic import BaseModel


class Config(BaseModel):
    """Plugin Config Here"""    
    QR_res:int = 5
