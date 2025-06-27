# zzky
​​External Collaboration Task 

## 一、项目整体架构设计

```
├── frontend/              # 前端项目 (React前端)
│   ├── public/
│   ├── src/
│   │   ├── api/              # API服务层
│   │   │   ├── index.js      # 统一封装
│   │   │   └── endpoints/    # 接口定义
│   │   ├── components/       # 可复用组件
│   │   │   ├── CanvasBase/   # 画布组件
│   │   │   ├── ModelCard/    # 模型卡片
│   │   │   └── Toolbar/      # 工具栏
│   │   ├── features/         # 业务模块
│   │   │   ├── detection/    # 检测模块
│   │   │   ├── synthesis/    # 合成模块
│   │   │   └── retrieval/    # 检索模块
│   │   ├── hooks/            # 自定义hooks
│   │   ├── store/            # Redux状态管理
│   │   ├── utils/            # 工具函数
│   │   ├── views/            # 页面视图
│   │   └── App.jsx
│   │
│   ├── config/               # 环境配置
│   ├── styles/               # 全局样式
│   └── tests/                # 测试用例
│
├── backend/                  # 后端服务 (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # 应用入口
│   │   ├── core/             # 核心配置
│   │   ├── schemas/          # Pydantic模型
│   │   ├── routers/          # API路由
│   │   ├── services/         # 业务逻辑
│   │   ├── utils/            # 工具函数
│   │   ├── models/           # 核心算法模块
│   │   │   ├── object_detection/
│   │   │   ├── image_synthesis/
│   │   │   ├── image_retrieval/
│   │   │   └── deepfake_detection/
│   ├── config/
│   │   ├── config.py         # 全局配置
│   │   └── settings.py       # 环境配置
│   ├── database/             # 数据库相关
│   ├── data/                 # 数据管理
│   │   ├── raw/              # 原始数据集
│   │   ├── processed/        # 预处理数据
│   │   └── synthetic/        # 合成数据集
│   ├── requirements/         # 依赖管理
│   └── scripts/              # 数据处理脚本
│
├── shared/                   # 共享资源
│   ├── configs/              # 全局配置
│   ├── docs/                 # 技术网页
│   └── scripts/              # 跨平台脚本
│
├── docker/
│   ├── Dockerfile.backend    # 后端镜像
│   └── Dockerfile.frontend   # 前端镜像
│
├── .env                      # 环境变量
├── docker-compose.yml        # 容器编排
└── README.md
```
