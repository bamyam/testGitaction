from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.dbfactory import db_startup

from app.routes.check import check_router
from app.routes.svc import svc_router
from app.routes.intro import intro_router
from app.routes.admin import admin_router
from app.routes.apply import apply_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    db_startup()

app = FastAPI(lifespan=lifespan)

# 세션처리를 미들웨어 설정
app.add_middleware(SessionMiddleware, secret_key='02232024duedate')


# 외부 route 파일 불러오기
app.include_router(check_router, prefix='/check')
app.include_router(svc_router, prefix='/svc')
app.include_router(intro_router, prefix='/intro')
app.include_router(admin_router, prefix='/admin')
app.include_router(apply_router, prefix='/apply')

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
app.mount('/static', StaticFiles(directory='views/static'), name='static')


@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html',{'request': req})    # 파일명과 넘길 데이터


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)