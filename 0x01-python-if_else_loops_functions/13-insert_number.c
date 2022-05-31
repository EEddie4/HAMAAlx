#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - a function
 * @head: the list head
 * @number: the number
 *
 * Return: adresse or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1, *ptr2, *nouveau;

	nouveau = malloc(sizeof(listint_t));

	if (nouveau == NULL)
		return (NULL);
	nouveau->n = number;

	ptr1 = *head;
	while (ptr1->n < number)
	{
		ptr2 = ptr1;
		ptr1 = ptr1->next;
	}
	ptr2->next = nouveau;
	nouveau->next = ptr1;
	return (nouveau);
}
