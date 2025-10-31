from app.config.database import Base, engine
import app.models  

print("Tạo bảng trong PostgreSQL...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Hoàn thành.")
