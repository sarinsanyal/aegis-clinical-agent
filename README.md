# Aegis Clinical Agent

AegisHealth Engine is a cloud-native, multi-container clinical platform designed for high-performance healthcare analytics and automated background task orchestration.   

## Core Functionality: 
    Processes structured EHR data in PostgreSQL alongside asynchronous, PII-sanitized LLM/RAG workflows using Celery and Redis.   
    
## Infrastructure & DevOps: 
    Fully containerized with Docker Compose and deployed automatically to AWS EC2 via a GitHub Actions CI/CD pipeline featuring unit testing.   