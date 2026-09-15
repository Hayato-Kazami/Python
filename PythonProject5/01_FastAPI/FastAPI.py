from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel, Field

app = FastAPI(title="JWT 鉴权练习", version="0.1.0")

# ---------- 配置（真实项目请放环境变量，别硬编码） ----------
SECRET_KEY = "practice-only-secret-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ---------- 写死的用户（练习用，生产要存数据库 + 加盐哈希） ----------
FAKE_USERNAME = "itheima"
FAKE_PASSWORD = "123456"

# tokenUrl 指向登录接口，/docs 页面的 Authorize 按钮靠它
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class Token(BaseModel):
    access_token: str
    token_type: str


class UserInfo(BaseModel):
    username: str


class ChatRequest(BaseModel):
    msg: str = Field(..., min_length=1, max_length=500)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """把用户名塞进 payload 的 sub 字段，加上过期时间后签名"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserInfo:
    """依赖函数：解析 Authorization 头里的 Bearer token，失败一律 401"""
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise cred_exc
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token 已过期，请重新登录",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except InvalidTokenError:
        raise cred_exc
    return UserInfo(username=username)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/login", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """校验用户名密码，通过则签发 JWT"""
    if form_data.username != FAKE_USERNAME or form_data.password != FAKE_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        {"sub": form_data.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=access_token, token_type="bearer")


@app.post("/chat")
def chat(
    req: ChatRequest,
    current_user: Annotated[UserInfo, Depends(get_current_user)],
):
    """受保护接口：必须带上有效 token 才能进"""
    return {
        "user": current_user.username,
        "reply": f"收到你的消息：{req.msg}",
    }



"""
app = FastAPI(...) 创建应用实例,整个项目的核心对象,title/version 会自动显示在文档页
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") 声明从 Authorization: Bearer ... 取 token,tokenUrl 让 /docs 出现 Authorize 按钮
class Token/UserInfo/ChatRequest Pydantic 模型。声明字段类型后 FastAPI 会自动做数据校验和文档生成——这是它比 Flask 强的地方
FAKE_USERNAME/FAKE_PASSWORD 写死的账号密码模拟数据源。真实项目这里会换成数据库查询 + 加盐哈希
create_access_token 把用户名塞进 payload 的 sub 字段、加上 exp 过期时间后 jwt.encode 签名
get_current_user 依赖函数。jwt.decode 解析 token 取 sub 作为用户名,失败一律抛 401(区分过期/非法)
@app.post("/login") 用 OAuth2PasswordRequestForm 收表单,校验通过后签发 token
@app.post("/chat") 受保护接口。Depends(get_current_user) 保证没带有效 token 就进不来
def 而非 async def 同步写法。FastAPI 会自动丢进线程池,不会因为阻塞拖慢其他请求
"""