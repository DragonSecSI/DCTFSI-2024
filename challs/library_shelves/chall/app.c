#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc -pie -fno-stack-protector -o app app.c

void setup() {
    alarm(60);
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

void hospital() {
    puts("How it the hell did I end up in hospital?!");
    system("/bin/sh");
}

void login() {
    char username[20];
    char password[9];

    puts("Plase log in to enter our library");
    printf("Username: ");
    fgets(username, 20, stdin);
    printf("Password: ");
    fgets(password, 9, stdin);
    printf("You are now logged in, ");
    printf(username);
    puts("\n");
}

void ready_reader() {
    char buf[64];

    puts("I am feeling ready. Ha ha, get it? Because I want to read.");
    puts("Anyways, give me your knowledge already.");
    fgets(buf, 0x64, stdin);
    puts("I am full now, I think I have to go puke...");
    puts("Bye");
}

int main() {
    setup();
    login();
    ready_reader();
    return 0;
}
