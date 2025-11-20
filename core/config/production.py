# -*- coding: utf-8 -*-
"""
Date:2021/5/21 3:24 下午
"""


# -*- coding: utf-8 -*-
"""
Date:2021/5/21 3:10 下午
"""

import os

from typing import Optional, Union

from pydantic import AnyHttpUrl, IPvAnyAddress
from pydantic_settings import BaseSettings
from typing import ClassVar
from commom.load_env import load_root_env

class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = False

    # 项目文档
    TITLE: str = "FastAPI+MySQL+Tortoise-orm项目生成"
    DESCRIPTION: str = "FastAPI 基于 Tortoise-orm 实现的大型项目框架"
    # 文档地址 默认为docs
    DOCS_URL: str = "/openapi/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/openapi/redoc"

    # token过期时间 分钟
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24

    # 生成token的加密算法
    ALGORITHM: str = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = '-%p-pg!$6^suoci%569f)d897sqf)g*a9gj7)i@py5ou$idirk_a'

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

    # RBAC 权限认证配置路径
    CASBIN_MODEL_PATH: ClassVar[str]= os.path.join(BASE_PATH, 'core/config/rbac_model.conf')

    # 超级管理员
    SUPER_USER: str = 'super'

    # 异常请求返回码
    HTTP_418_EXCEPT: int = 418


    # 配置你的Mysql环境
    MYSQL_USERNAME: str = os.getenv("MYSQL_USERNAME")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress, str] = os.getenv("MYSQL_HOST")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")

    # Mysql地址
    SQLALCHEMY_DATABASE_URL: str = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis地址
    REDIS_HOST:  Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("REDIS_HOST")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 63034))

    class Config:
        env_file = ".env"

settings = Settings()
