#include <stdlib.h>
#include <stdio.h>

#ifndef FLAG
#define FLAG {0}
#error Run build.py instead!
#endif

int main() {
    char buff[0x100];
    char flag[] = FLAG;
    printf("Flag? ");
    fgets(buff, sizeof(buff), stdin);
    for (int i = 0; i < sizeof(flag); i++) {
        if (flag[i] != buff[i]) {
            puts("Try again!");
            return 1;
        }
    }
    puts("Correct!");
    return 0;
}
