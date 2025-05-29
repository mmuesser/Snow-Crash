#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int ac, char **av)
{
    int fd = open(av[1], O_RDONLY);
    char c;
    int i = 0;
    while (read(fd, &c, 1))
    {
        printf("%c", c - i);
        i++;
    }
    printf("\n");
    return (0);
}