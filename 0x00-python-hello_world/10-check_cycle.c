#include "lists.h"

/**
 *check_cycle - checks if a linked list contains a cycle
 *@list: linked list to check
 *
 *Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{

	listint_t *eleph, *cheetah;

	if (list == NULL || list->next == NULL)
		return (0);
		
	listint_t *eleph = list;
	listint_t *cheetah = list;


	for (; eleph && cheetah && cheetah->next; eleph = eleph->next, cheetah = cheetah->next->next)
	{
		if (eleph == cheetah)
			return (1);
	}

	return (0);
}
