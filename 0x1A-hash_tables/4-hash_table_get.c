#include "hash_tables.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * hash_djb2 - return the hash of djb2
 * @str: string to compute str dfbe2 hash
 * Return: djb2_hash value of string
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
hash_node_t *t = ht->array[0];
while (t != NULL)
{
if (t->key == key)
{
return (t->value);
}
t = t->next;
}

return (NULL);

}