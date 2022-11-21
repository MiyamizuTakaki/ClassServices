from datetime import datetime, timedelta
from typing import Optional
import jwt
SECRET_KEY = '17b725c66396f9a86406809a4c823fe67bb7a05d68def80ab0718a8cde34d4ac'
ALGORITHM = "HS256"
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    # 检测token的有效时间是否为空，如果为空，则默认设置有效时间为15分钟
    if expires_delta: 
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=90)
    # 更新到我们之前传进来的字典
    to_encode.update({"exp": expire})
    # jwt 编码 生成我们需要的token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt