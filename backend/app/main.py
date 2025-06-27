from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 实例
app = FastAPI(title="zzky API 服务", version="1.0.0")

# CORS 配置（允许所有来源，生产环境请按需调整）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由注册（示例，后续可在 routers 目录添加并引入具体路由）
# from app.routers import example_router
# app.include_router(example_router.router)

@app.get("/")
def read_root():
    return {"message": "zzky FastAPI 后端已启动"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
