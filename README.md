# Bilibili MCP 服务器

这是一个用于与Bilibili API交互的MCP服务器项目。

## 功能特性

- 提供Bilibili API的通用搜索功能
- 支持通过MCP协议与其他系统集成

## 安装

1. 确保已安装Python 3.10+（由.python-version指定）
2. 使用uv安装依赖：
   ```bash
   uv pip install -r requirements.txt
   ```

## 使用

启动MCP服务器：
```bash
uv --directory /Users/zao/project/bilibili-mcp-server run bilibili.py
```

## 依赖管理

- 依赖项由pyproject.toml定义
- 使用uv.lock锁定依赖版本

## 贡献

欢迎提交Pull Request。请确保：
- 代码符合PEP 8规范
- 添加必要的单元测试
- 更新相关文档

## 许可证

MIT