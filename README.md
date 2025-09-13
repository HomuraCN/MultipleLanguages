# Python & C++ Hybrid Programming Demo

这是一个简单的示例，展示了如何使用 Python 调用 C++ 编译的动态库来加速计算密集型任务。

## 依赖环境

- Python 3.x
- C++ 编译器 (本项目使用 Visual Studio 2022 on Windows)

## 如何运行

1.  **克隆仓库**
    
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    
2.  **编译 C++ 模块**

    **For Windows (使用 Visual Studio 2022):**
    - 打开 "x64 Native Tools Command Prompt for VS 2022"。
    - 进入项目根目录。
    - 执行以下命令来编译生成 `calculator.dll`:
      ```cmd
      cl.exe /LD calculator.cpp
      ```

    **(可选) For Linux:**
    ```bash
    g++ -shared -fPIC -o calculator.so calculator.cpp
    ```

3.  **运行 Python 主程序**
    确保你的 Python 环境已经激活，然后执行：
    
    ```bash
    python main.py
    ```

---

### 备选方案：通过 GitHub Releases 提供预编译包

如果你觉得让每个用户都手动编译太麻烦，还有一个折中的专业方案：

1.  **不要**将 `.dll` 文件直接提交到你的代码分支里。
2.  在你的 GitHub 仓库页面，创建一个 **"Release" (发行版)**。
3.  你可以自己为 Windows, macOS, Linux 分别编译好对应的库文件（`.dll`, `.so`, `.dylib`），然后将它们打包成 zip 文件，**作为附件上传到这个 Release 页面**。

这样，你的 Git 仓库历史保持了干净（只包含源代码），而需要便捷安装的用户可以直接从 Release 页面下载已经编译好的版本。

对于你目前的学习项目，强烈推荐采用**最佳实践**方案：**创建 `.gitignore` 并完善 `README.md` 中的编译指南**。这是成为一个优秀开发者的必经之路。
