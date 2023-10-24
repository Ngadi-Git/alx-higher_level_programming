#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *obj)
{
	Py_ssize_t size, alloc, i;
	const char *type_name;

	if (!PyList_Check(obj))
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	PyListObject *list = (PyListObject *)obj;
	PyVarObject *var = (PyVarObject *)obj;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];

		type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
		else if (strcmp(type_name, "float") == 0)
		{
			print_python_float(item);
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */


void print_python_float(PyObject *obj)
{
	const char *type_name = obj->ob_type->tp_name;

	if (strcmp(type_name, "float") != 0)
	{
		fprintf(stderr, "[.] float object info\n");
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}

	PyFloatObject *float_obj = (PyFloatObject *)obj;
	double value = float_obj->ob_fval;

	char *buffer = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("[.] float object info\n");
	printf("  value: %s\n", buffer);

	PyMem_Free(buffer);
} 
