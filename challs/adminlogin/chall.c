#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void vuln() {
    char name[32];
    int passcode = 0;
    printf("Login: ");
    gets(name);

    if(!strcmp(name, "admin") && passcode == 0x1337c0de)
    {
        puts("Welcome, admin\n");
        system("/bin/sh");
        return;
    }

    puts("You do not have access to this machine!");
    puts("This incident will be reported!!");
    // TODO: log and report the incident
}

int main() {
    alarm(10);
    vuln();
    return 0;
}
