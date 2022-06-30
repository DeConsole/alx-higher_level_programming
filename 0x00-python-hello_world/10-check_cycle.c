#include "lists.h"
/**
 * check_cycle - checks a cycle in a single link list in it
 * @list: singly list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list->next;

	while (current != NULL)
{
	if (current == list)
		return (1);
	current = current->next;
}

	return (0);
}
