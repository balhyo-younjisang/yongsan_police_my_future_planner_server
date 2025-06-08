from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# UserAnswers 요청 스키마 (생성용)
class UserAnswersCreate(BaseModel):
    gender: str
    age: int
    school_level: str

    career_goal: Optional[str] = None
    hobbies: Optional[List[str]] = None
    smartphone_time: Optional[str] = None
    emotions: Optional[List[str]] = None
    stress_coping: Optional[str] = None
    drug_opinion: Optional[str] = None
    drug_response: Optional[str] = None
    future_hope: Optional[str] = None


# UserAnswers 응답 스키마 (읽기용)
class UserAnswersResponse(UserAnswersCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Result 요청 스키마 (생성용)
class ResultCreate(BaseModel):
    user_answers_id: int
    career_goal: Optional[str] = None
    future_positive: str
    future_negative: str
    image_positive: Optional[str] = None
    image_negative: Optional[str] = None
    score_risk: Optional[int] = None
    recommended_tip: Optional[str] = None
    tag: Optional[List[str]] = None


# Result 응답 스키마 (읽기용)
class ResultResponse(ResultCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
