// calculator.cpp

// extern "C" �ǹؼ��������߱�������C���Եķ�ʽ�����������������ֹ���������ı�
extern "C" {
    // __declspec(dllexport) �� Windows ���еģ���ʾ�������Ҫ�� DLL �е������Ա�����������Ե���
    __declspec(dllexport) long long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}