import logging
import httpx
import os
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

app = FastAPI()

logger.info(f'Your vercel webhook url: {os.environ.get("VERCEL_WEBHOOK_URL")}')

class VerifyToken(BaseModel):
    verification_token: str | None = None

@app.post('/update')
async def update(verify_token: VerifyToken):
    if verify_token.verification_token is not None:
        logger.info(f'Your verify token: {verify_token.verification_token}')
    httpx.post(os.environ.get('VERCEL_WEBHOOK_URL'))
    return "success"