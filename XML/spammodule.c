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
	{NULL, NULL, 0, NULL} // <- �迭 �� ǥ��.
};

static PyModuleDef spammodule = {			//2. ������ ��� ������ ��� ����ü
		PyModuleDef_HEAD_INIT,
		"spam",
		"It is a test module.",
		-1, SpamMethods						//3. SpamMethods �迭 ����
};

//1. ���̽� ���������Ϳ��� import�� �� ���� (PyInit_<module> �Լ�)
PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule);	//2. spammodule ����ü ����
}