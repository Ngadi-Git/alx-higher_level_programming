#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints basic details about the pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);
	int index;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (index = 0; index < len; index++)
		printf("Element %i: %s\n", index, Py_TYPE(obj->ob_item[index])->tp_name);
}
