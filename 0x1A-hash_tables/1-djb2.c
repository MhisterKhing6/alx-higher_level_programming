#include "hash_tables.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * hash_djb2 - return the hash of djb2
 * @str: string to compute str dfbe2 hash
 * Return: djb2_hash value of string
 */
unsigned long int hash_djb2(const unsigned char *str)
{
unsigned long  result = 5381;
int character;
while ((character = *str++))
{
result = ((result << 5) + result)+character;
}

return (result);
}