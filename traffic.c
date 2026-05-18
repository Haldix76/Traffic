#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

void sendSignal(int pid, int sig)
{
    if (kill(pid, sig) == -1)
    {
        perror("kill");
    }
    else
    {
        printf("Signal %d sent to PID %d\n", sig, pid);
    }
}

void newProcess(void)
{
    pid_t pid = fork();

    if (pid == 0)
    {
        execlp("kwrite", "kwrite", NULL);

        perror("execlp");
        exit(0);
    }
    else
    {
        printf("New process created! PID = %d\n", pid);
    }
}

int main(int argc, char *argv[])
{
    if (argc == 4 && strcmp(argv[1], "signal") == 0)
    {
        int pid = atoi(argv[2]);
        int sig = atoi(argv[3]);

        sendSignal(pid, sig);
    }

    else if (argc == 2 && strcmp(argv[1], "new") == 0)
    {
        newProcess();
    }

    else
    {
        printf("Usage:\n");
        printf("./traffic signal <pid> <signal>\n");
        printf("./traffic new\n");
    }

    return 0;
}