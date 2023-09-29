#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - create infinite loop
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
        sleep(1);
    return (0);
}

/**
 * main - create 5 zombie processe
 * Return: 0
*/
int main(void)
{
	pid_t zombie_pid;
	unsigned int i = 0;

	for (; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	return (infinite_while());
}
