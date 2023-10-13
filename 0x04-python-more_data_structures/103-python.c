#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints the basic info about lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int bfr, m_alloc, index;
	const char *kind;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	bfr = var->ob_size;
	m_alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", bfr);
	printf("[*] Allocated = %d\n", m_alloc);

	index = 0;
	while (index < bfr)
	{
		kind = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, kind);
    
		if (strcmp(kind, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		index++;
	}
}

/**
 * print_python_bytes - Prints basic info about the byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char index, bfr;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		bfr = 10;
	else
		bfr = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", bfr);
	for (index = 0; index < bfr; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (bfr - 1))
			printf("\n");
		else
			printf(" ");
	}
}
