#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *runner1 = list;
	listint_t *runner2 = list;

	if (!list)
		return (0);
	while (runner1 && runner2 && runner2->next)
	{
		runner1 = runner1->next;
		runner2 = runner2->next->next;
		if (runner1 == runner2)
			return (1);
	}

	return (0);
}
