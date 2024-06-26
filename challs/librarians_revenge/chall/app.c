#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc -pie -fstack-protector -o app app.c

char* magic_word = "/bin/sh\0";

void set_helpers() {
    asm("pop %rdi");
    asm("ret");
    asm("pop %rsi");
    asm("ret");
    asm("pop %rdx");
    asm("ret");
}

void setup() {
    alarm(60);
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

void hospital(int social_security_number, int money, char* magic) {
    puts("Finally, hospital!");
    if (!social_security_number) {
        puts("No social security number provided.");
        exit(1);
    }
    if (money < 0xdeadb33f) {
        puts("Not enough money on your bank account, sorry!");
        exit(1);
    }
    puts("Right this way, sir.");
    system(magic);
    exit(0);
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
    char buf[100];

    puts("I am feeling ready. Ha ha, get it? Because I want to read.");
    puts("Anyways, give me your knowledge already.");
    fgets(buf, 0x100, stdin);
    puts("I am full now, I think I have to go puke...");
    puts("I think I need to go to the hospital, I feel ill.");
    puts("Bye");
}

int main() {
    setup();
    login();
    ready_reader();
    return 0;
}
