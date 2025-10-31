from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.setting_schema import SettingResponse, SettingUpdate
from app.services import setting_service


class SettingController:
    def __init__(self):
        self.service = setting_service

    def get_setting(self, db: Session = Depends(get_db)) -> SettingResponse:
        """Lấy bản ghi cấu hình (tự tạo nếu chưa có)"""
        setting = self.service.create_default_setting(db)
        if not setting:
            raise HTTPException(status_code=404, detail="Không thể khởi tạo Setting.")
        return setting

    def update_setting(self, data: SettingUpdate, db: Session = Depends(get_db)) -> SettingResponse:
        """Cập nhật thông tin cấu hình"""
        setting = self.service.update_setting(db, data)
        return setting
