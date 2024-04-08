#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void vuln() {
    char name[32];
    long i1 = 0;
    long i2 = 0;
    printf("What's your name? ");
    scanf("%31s", name);
    printf("Okay %s, throw me some numbers\n", name);
    scanf("%lu", &i1);
    scanf("%lu", &i2);

    if(i1 > 0 && i2 > 0 && i1 + i2 < 0) {
        puts("Yeah, that fits");
        system("/bin/sh");
        return;
    }

    printf("%s, it's 1 fucking 30 in the morning, what are you doing calling me?\n", name);
}

int main() {
    alarm(10);
    vuln();
    return 0;
}
