from app.db import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE patient_records ADD COLUMN IF NOT EXISTS clinical_summary TEXT;"))
    conn.commit()
    print("Migration successful: Added 'clinical_summary' column.")