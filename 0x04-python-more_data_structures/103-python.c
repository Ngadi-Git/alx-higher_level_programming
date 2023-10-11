#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - displays the basic info about the Python lists to the screen..
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int bfer, bytes, index;
	const char *chr;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	bfer = var->ob_size;
	bytes = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", bfer);
	printf("[*] Allocated = %d\n", bytes);

	for (index = 0; index < size; index++)
	{
		chr = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, chr);
		if (strcmp(chr, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - displayss the basic info about Python byte objects to the screen.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char index, bfer;
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
		bfer = 10;
	else
		bfer = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", bfer);
	for (index = 0; index < bfer; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (bfer - 1))
			printf("\n");
		else
			printf(" ");
	}
}
