#include <Python.h>
#include <string.h>

static PyObject* spam_strlen(PyObject* self, PyObject* args) {
	char* str;
	int len;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	len = strlen(str);
	return Py_BuildValue("i", len);
}

static PyMethodDef SpamMethods[] = {
	//{"division", spam_division, METH_VARARGS, "division function"},
	{"strlen", spam_strlen, METH_VARARGS, "count a string length."},
	{NULL, NULL, 0, NULL} // <- 배열 끝 표시.
};

static PyModuleDef spammodule = {			//2. 생성할 모듈 정보를 담는 구조체
		PyModuleDef_HEAD_INIT,
		"spam",
		"It is a test module.",
		-1, SpamMethods						//3. SpamMethods 배열 참조
};

//1. 파이썬 인터프리터에서 import할 때 실행 (PyInit_<module> 함수)
PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule);	//2. spammodule 구조체 참조
}