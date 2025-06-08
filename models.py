import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship  
from yongsan_police_my_future_planner_server.database import Base

class UserAnswers(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, index=True)  # 설문 응답 고유 ID (기본키)
    gender = Column(String(10), nullable=False)         # 성별 (예: "남", "여" 또는 "0", "1")
    age = Column(Integer, nullable=False)               # 나이 (정수)
    school_level = Column(String(20), nullable=False)   # 학교 단계 (예: "초등", "중등", "고등")

    career_goal = Column(String(100), nullable=True)         # 희망 진로 또는 직업
    hobbies = Column(JSON, nullable=True)                    # 취미 목록 (JSON 배열)
    smartphone_time = Column(String(50), nullable=True)      # 하루 스마트폰 사용 시간 (예: "1~2시간")
    emotions = Column(JSON, nullable=True)                   # 최근 느낀 감정들 (JSON 배열)
    stress_coping = Column(String(100), nullable=True)       # 스트레스 대처 방법
    drug_opinion = Column(String(100), nullable=True)        # 마약에 대한 생각이나 의견
    drug_response = Column(String(100), nullable=True)       # 만약 마약을 권유받았을 때 대응 방법
    future_hope = Column(Text, nullable=True)                # 미래에 대한 희망이나 바람 (자유 서술)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # 응답 생성 시간 (자동 기록)

    result = relationship("Result", back_populates="user_answers", uselist=False)  
    # 한 명의 사용자 응답에 대응하는 결과(Result) 하나와 1:1 관계 설정


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, index=True)                    # 결과 고유 ID
    user_answers_id = Column(Integer, ForeignKey("user_answers.id"), nullable=False)  # 설문 답변 연결 FK
    created_at = Column(DateTime, default=datetime.datetime.utcnow)      # 결과 생성 시간

    career_goal = Column(String(100), nullable=True)                     # 설문에서 받은 진로 목표 (복사 저장)
    future_positive = Column(Text, nullable=False)                       # 마약 선택 안했을 때 긍정적 미래 시나리오
    future_negative = Column(Text, nullable=False)                       # 마약 선택 했을 때 부정적 미래 시나리오

    image_positive = Column(String(255), nullable=True)                  # 긍정적 미래 이미지 URL (옵션)
    image_negative = Column(String(255), nullable=True)                  # 부정적 미래 이미지 URL (옵션)

    score_risk = Column(Integer, nullable=True)                          # 위험 점수 (예: 0~100)
    recommended_tip = Column(Text, nullable=True)                        # 맞춤형 예방 조언

    tag = Column(JSON, nullable=True)                                    # 관련 키워드 태그 리스트 (JSON 배열)

    user_answers = relationship("UserAnswers", back_populates="result")  # 역참조 관계
