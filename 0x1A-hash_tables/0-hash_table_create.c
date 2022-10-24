#include "hash_tables.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * hash_table_create - return a pointer to a hash table object
 * @size: size of hashtable array
 * Return: hashtable structure
 */
hash_table_t *hash_table_create(unsigned long int size)
{
hash_table_t *t = (hash_table_t *)malloc(sizeof(hash_table_t));
hash_node_t *temp = (hash_node_t *)malloc(sizeof(hash_node_t) * size);
if (t == NULL)
{
return (NULL);
}
t->size = size;
 
if (temp == NULL)
{
return (NULL);
}
t->array = &temp;
return (t);

}
