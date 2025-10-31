from sqlalchemy.orm import Session
from app.models.setting_model import Setting
from app.schemas.setting_schema import SettingCreate, SettingUpdate

"""Lấy bản ghi duy nhất trong bảng setting"""
def get_setting(db: Session):
    return db.query(Setting).first()

"""Tạo giá trị mặc định nếu chưa tồn tại"""
def create_default_setting(db: Session):
    setting = get_setting(db)
    if setting:
        return setting

    new_setting = Setting()
    db.add(new_setting)
    db.commit()
    db.refresh(new_setting)
    return new_setting

"""Cập nhật thông tin cấu hình"""
def update_setting(db: Session, data: SettingUpdate):
    setting = get_setting(db)
    if not setting:
        setting = create_default_setting(db)

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(setting, field, value)

    db.commit()
    db.refresh(setting)
    return setting