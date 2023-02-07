from fastapi import APIRouter, Depends

from auth.base_config import current_user
from tasks.tasks import send_email_report

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report.delay(user.username)
    return {
        "status": 200,
        "data": "Email send",
        "details": "Teriyaisa"
    }