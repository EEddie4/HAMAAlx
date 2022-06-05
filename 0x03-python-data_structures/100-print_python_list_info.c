#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>


/**
 * print_python_list_info - check the code for
 * @p: object
 *
 * Return: Always 0.
 */
void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python list = ");
	printf("[*] Allocated = ");
	return (0);
}
