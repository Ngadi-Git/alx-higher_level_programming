#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If it fails - return NULL.
 *         Otherwise - return a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodal = *head, *newptr;

	new = malloc(sizeof(listint_t));
	if (newptr == NULL)
		return (NULL);
	newptr->n = number;

	if (nodal == NULL || nodal->n >= number)
	{
		newptr->next = nodal;
		*head = newptr;
		return (newptr);
	}

	while (nodal && nodal->next && nodal->next->n < number)
		nodal = nodal->next;

	newptr->next = nodal->next;
	nodal->next = newptr;

	return (newptr);
}
