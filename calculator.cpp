// calculator.cpp

// extern "C" 是关键，它告诉编译器以C语言的方式来编译这个函数，防止函数名被改变
extern "C" {
    // __declspec(dllexport) 是 Windows 特有的，表示这个函数要从 DLL 中导出，以便其他程序可以调用
    __declspec(dllexport) long long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}