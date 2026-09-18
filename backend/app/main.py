from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import get_db, engine, Base
from app import models

# Automatically create tables in PostgreSQL on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AegisHealth Engine")

@app.get("/")
def root(db: Session = Depends(get_db)):
    try:
        # Executes a simple query to test the active connection
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"

    return {
        "status": "online", 
        "message": "AegisHealth API is running",
        "database": db_status
    }

@app.post("/patients/")
def create_patient(name: str, history: str, db: Session = Depends(get_db)):
    patient = models.PatientRecord(patient_name=name, medical_history=history)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return {"status": "success", "patient": patient}

@app.get("/patients/{patient_id}")
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.PatientRecord).filter(models.PatientRecord.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient