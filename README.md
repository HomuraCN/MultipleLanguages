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
