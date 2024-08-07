from typing import List, Union, Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    @field_validator('email')
    def check_required_fields(cls, v):
        if v is None:
            raise ValueError(f'{cls.__name__} is a required field')
        return v

class UserCreate(UserBase):
    password: str
    @field_validator('password')
    def check_required_fields(cls, v):
        if v is None:
            raise ValueError(f'{cls.__name__} is a required field')
        return v

class User(UserBase):
    user_id: int
    age: Optional[int] = Field(default=None)
    height: Optional[float] = Field(default=None)
    weight: Optional[float] = Field(default=None)
    workout_duration: Optional[int] = Field(default=None)
    workout_frequency: Optional[int] = Field(default=None)
    workout_goal: Optional[int] = Field(default=None)
    role: str
    
    class ConfigDict(ConfigDict):
        from_attributes = True

class UserUpdate(BaseModel):
    current_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_password: Optional[str] = None
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    workout_duration: Optional[int] = None
    workout_frequency: Optional[int] = None
    workout_goal: Optional[int] = None

class TrainerBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    def check_required_fields(cls, v):
        if v is None:
            raise ValueError(f'{cls.__name__} is a required field')
        return v

class TrainerCreate(TrainerBase):
    password: str
    
    @field_validator('password')
    def check_required_fields(cls, v):
        if v is None:
            raise ValueError(f'{cls.__name__} is a required field')
        return v

class Trainer(TrainerBase):
    trainer_id: int
    hashed_password: str
    role: str
    
class TrainerUpdate(BaseModel):
    current_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_password: Optional[str] = None

class ConnectedUserInfo(BaseModel):
    user_id: int
    age: Optional[int]
    height: Optional[float]
    weight: Optional[float]
    workout_duration: Optional[int]
    workout_frequency: Optional[int]
    workout_goal: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]

    class ConfigDict(ConfigDict):
        from_attributes = True
    
class MappingStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"

class UserMappingInfo(BaseModel):
    user_id: int
    user_email: str
    user_first_name: str
    user_last_name: str
    status: MappingStatus

class TrainerMappingInfo(BaseModel):
    trainer_id: int
    trainer_email: str
    trainer_first_name: str
    trainer_last_name: str
    status: MappingStatus

class CreateTrainerUserMapping(BaseModel):
    other_id: int

class TrainerUserMappingResponse(BaseModel):
    id: int
    trainer_id: int
    user_id: int
    status: str

class TrainerUserMappingUpdate(BaseModel):
    new_status: str

class Message(BaseModel):
    message: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None