from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db import Base

class PatientRecord(Base):
    __tablename__ = "patient_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(100), nullable=False)
    medical_history = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())