from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.setting_schema import SettingResponse, SettingUpdate
from app.controller.setting_controller import SettingController

router = APIRouter(prefix="/setting", tags=["Setting"])
controller = SettingController()


@router.get("/", response_model=SettingResponse)
def get_setting(db: Session = Depends(get_db)):
    """Lấy thông tin cấu hình"""
    return controller.get_setting(db)


@router.put("/", response_model=SettingResponse)
def update_setting(data: SettingUpdate, db: Session = Depends(get_db)):
    """Cập nhật thông tin cấu hình"""
    return controller.update_setting(data, db)

setting_route = router