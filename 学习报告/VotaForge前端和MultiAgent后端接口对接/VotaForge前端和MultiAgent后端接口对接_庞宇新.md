# VotaForge 前端和 MultiAgent 后端接口对接

以 GPF 客户端为例 | 4 步搞定

---

## 步骤一：下载 GPF 版本

### 操作

- 访问 GPF 版本下载页面：`http://14.18.100.250:8989/release/GPF/`
- 选择需要的版本进行下载（下载对应版本号的 `.zip` 压缩包）

![图 1：GPF 版本下载页](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图1.png)

---

## 步骤二：打开 GPF 客户端

### 操作

- 打开 GPF 客户端（可通过 BAP 插件「打开管理工具」进入）

![图 2：GPF 客户端界面](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图2.png)

---

## 步骤三：配置并登录

### 操作

- 在登录界面填写以下信息：

| 字段 | 值 |
|------|----|
| WS 地址 | `ws://14.18.100.250:18126/` |
| 用户名 | `panelx` |
| 密码 | `panelx123!@#` |

- 确认信息无误后，点击「连接」登录

![图 3：登录界面填写信息](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图3.png)

![图 4：点击连接登录](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图4.png)

---

## 步骤四：删除并拉取工程版本

### 操作

- 登录成功后，在 GPF 客户端中**先删除需要更新的工程**
- 再从仓库**拉取需要的对应版本**

![图 5：GPF 客户端主界面](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图5.png)

![图 6：删除旧工程并拉取新版本](../assets/VotaForge前端和MultiAgent后端接口对接_庞宇新_assets/图6.png)

---

## 操作总结

| # | 操作 | 说明 |
|---|------|------|
| 1 | 下载 GPF 版本 | 访问 `http://14.18.100.250:8989/release/GPF/` 下载对应版本 `.zip` |
| 2 | 打开 GPF 客户端 | BAP 插件 → 打开管理工具 |
| 3 | 填写登录信息 | WS: `ws://14.18.100.250:18126/`，用户: `panelx`，密码: `panelx123!@#` |
| 4 | 删除旧工程并拉取新版本 | 在 GPF 客户端中完成版本更新 |
