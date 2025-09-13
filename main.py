# main.py
import ctypes
import time
import platform
import os

# --- 纯 Python 实现的斐波那契函数，用于对比性能 ---
def python_fibonacci(n):
    if n <= 1:
        return n
    return python_fibonacci(n - 1) + python_fibonacci(n - 2)

# --- 加载 C++ 共享库并调用其函数 ---
def cpp_fibonacci(n):
    # 1. 确定库文件的路径
    # 在 Windows 上，Visual Studio 编译的 DLL 通常叫 .dll
    lib_path = os.path.join(os.path.dirname(__file__), 'calculator.dll')
        
    try:
        # 使用 ctypes 加载 DLL
        calculator_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"加载库失败: {e}")
        print(f"请确保 '{lib_path}' 文件存在。")
        print("你是否已经成功执行了 C++ 编译步骤？")
        return None

    # 2. 定义 C++ 函数的参数类型和返回类型
    fib_func = calculator_lib.fibonacci
    fib_func.argtypes = [ctypes.c_int]      # 参数是一个 int
    fib_func.restype = ctypes.c_longlong # 返回值是一个 long long

    # 3. 直接调用 C++ 函数
    return fib_func(n)

# --- 主程序 ---
if __name__ == "__main__":
    number = 40

    # --- 测试纯 Python 版本 ---
    print(f"正在使用纯 Python 计算 fibonacci({number})...")
    start_time_py = time.time()
    result_py = python_fibonacci(number)
    end_time_py = time.time()
    py_duration = end_time_py - start_time_py
    print(f"Python 结果: {result_py}")
    print(f"Python 耗时: {py_duration:.4f} 秒\n")

    # --- 测试 C++ 加速版本 ---
    print(f"正在使用 C++ 库计算 fibonacci({number})...")
    start_time_cpp = time.time()
    result_cpp = cpp_fibonacci(number)
    end_time_cpp = time.time()
    
    if result_cpp is not None:
        cpp_duration = end_time_cpp - start_time_cpp
        print(f"C++ 结果: {result_cpp}")
        print(f"C++ 耗时: {cpp_duration:.4f} 秒")

        if cpp_duration > 0:
            speedup = py_duration / cpp_duration
            print(f"\n在此任务上，C++ 大约比 Python 快 {speedup:.2f} 倍。")