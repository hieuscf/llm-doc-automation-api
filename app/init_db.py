from app.config.database import Base, engine
from app.models import source_model

print("Tạo bảng trong PostgeSQL...")
Base.metadata.create_all(bind=engine)
print("Hoàn thành.")