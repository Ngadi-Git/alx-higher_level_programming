#include "lists.h"

/**
 * insert_node - Inserts a digit into a sorted singly-linked list.
 * @head: the linked list head pointer
 * @number: The number to insert.
 * 
 * Return: If the function fails - returns NULL.
 *         Otherwise - returns a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
