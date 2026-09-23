# Git / GitHub 完整设置流程（含报错排查）

> 用途：把这个仓库从本地推到 GitHub。**你已完成的步骤打了 ✅。**
> 最后更新：2026-09-23

---

## 一、当前进度

| # | 步骤 | 状态 |
|---|---|---|
| 1 | 注册 / 登录 GitHub | ✅ 已完成（浏览器已登录） |
| 2 | 本地配置 git 身份 | ✅ 已完成（`liuziguang` / `1310612977@qq.com`） |
| 3 | 本地初始化仓库并提交 | ✅ 已完成（commit `71df249`，12 files） |
| 4 | 添加 remote | ✅ 已完成（指向 `github.com/liuziguang/quantum-journey.git`） |
| 5 | **在 GitHub 网页上创建空仓库** | ❌ **← 卡在这里** |
| 6 | push 到 GitHub | ⏳ 等第 5 步 |

---

## 二、你遇到的报错

```
$ git push -u origin main
remote: Repository not found.
fatal: repository 'https://github.com/liuziguang/quantum-journey.git/' not found
```

**含义**：GitHub 上不存在 `liuziguang/quantum-journey` 这个仓库。
Git 本身没问题，remote 地址也写对了——**只是远端还没有那个"容器"**。

> 补充：如果你已经建了仓库但还是这个报错，那有两种可能：
> ① 仓库名或用户名拼写不一致（GitHub 用户名**不区分大小写**，但仓库名区分）
> ② 仓库是 Private，而你的凭据没生效（未认证访问私有仓库也会返回 404）
> ③ remote 地址写错 → 用 `git remote -v` 检查，用 `git remote set-url origin <新地址>` 修改

---

## 三、解决步骤（3 分钟）

### 第 1 步：在浏览器创建空仓库

1. 打开 **https://github.com/new**
2. **Repository name** 填：`quantum-journey`
   （必须和 remote 地址里的名字**完全一致**）
3. **Description**（可选）：`从理论物理转向量子计算软件/算法的学习工作区`
4. 选择可见性：
   - **Public（推荐）**——这是你的**求职作品集**，招聘方需要能点开看
   - Private——也可以，但求职时你得手动加对方为协作者，不方便
5. ⚠️ **关键：这三个都不要勾**
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
   （勾了会产生一个远端 commit，导致 push 时出现 `rejected — fetch first` 冲突。**必须是完全空的仓库**）
6. 点 **Create repository**

### 第 2 步：回到 PowerShell 推送

```powershell
cd D:\Quantum_Info\practice\quantum-journey
git push -u origin main
```

### 第 3 步：授权

- 会**自动弹出浏览器窗口**要求授权 GitHub（Git for Windows 自带 Credential Manager）
- 点 **Authorize** 即可，之后本机就记住了
- 如果没弹窗或报 `403`：需要手动创建 **Personal Access Token**
  路径：GitHub → 右上角头像 → Settings → Developer settings
  → Personal access tokens → **Tokens (classic)** → Generate new token
  → 勾选 **`repo`** 权限 → 复制 token
  → push 时把 token 当密码粘贴

### 第 4 步：验证

```powershell
git log --oneline -1
git remote -v
git status
```

然后刷新 GitHub 页面，应该能看到 12 个文件。

---

## 四、如果用户名不对

你构造的地址是 `github.com/liuziguang/...`。请确认这是你的**真实 GitHub 用户名**：

- 登录 GitHub 后，看右上角头像旁边的用户名，或访问 https://github.com/settings/profile
- 如果不对，改 remote：
  ```powershell
  git remote set-url origin https://github.com/<正确用户名>/quantum-journey.git
  ```

---

## 五、顺手把 git 身份设成全局（建议）

你这次是在仓库内设置的（`git config`，不带 `--global`），只对这个仓库生效。
以后新建仓库还要再设一次。建议改成全局：

```powershell
git config --global user.name "liuziguang"
git config --global user.email "1310612977@qq.com"
```

---

## 六、日常提交习惯（从 Week 2 开始）

```powershell
git status                      # 看改了什么
git add -A                      # 暂存全部改动
git commit -m "week02: 完成 XXX" # 提交（写清做了什么）
git push                        # 推到 GitHub
```

**规则：每个可见产物一次 commit。** commit 记录连续、信息清晰，本身就是给招聘方看的信号。

---

## 七、常见报错速查

| 报错 | 原因 | 解决 |
|---|---|---|
| `Repository not found` | 远端仓库不存在 / 名字或用户名错 / 私有仓库未认证 | 见第三节 |
| `rejected — fetch first` | 远端有你本地没有的 commit（建仓库时勾了 README） | `git pull --rebase origin main` 后再 push |
| `src refspec main does not match any` | 本地没有 `main` 分支（还在 `master`） | `git branch -M main` |
| `Authentication failed` | 凭据过期或用了密码而非 token | 用 Personal Access Token；或删掉 Windows 凭据管理器中 github.com 的条目后重试 |
| `Permission denied (publickey)` | 用了 SSH 地址但没配 key | 改用 HTTPS 地址，或配置 SSH key |
| 中文文件名显示成 `\345\221\250...` | Git 默认转义非 ASCII 文件名 | `git config --global core.quotepath false` |
| `LF will be replaced by CRLF` | Windows 换行符警告 | **无害**，可忽略 |

---

*文件：`practice/quantum-journey/GIT_SETUP.md`*
