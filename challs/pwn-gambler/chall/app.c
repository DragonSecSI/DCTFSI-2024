#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

unsigned long long setup() {
	unsigned long long retval;

	alarm(60);
	setbuf(stdin, 0);
	setbuf(stdout, 0);

	int fd = open("/dev/random", O_RDONLY);
	read(fd, &retval, 8);
	close(fd);
	return retval;
}

static void win()
{
	system("/bin/sh");
}

void vuln()
{
	size_t length;
	char buf[64];
	length = read(0, buf, 64);
	buf[length - 1] = '\0';
	printf(buf);
}

int main()
{
	unsigned long long rn, guess;

	rn = setup();
	printf("Hello, feeling lucky? ");
	vuln();
	puts("?! We will see about that");
	sleep(1);
	printf("Take a guess: ");
	scanf("%llu", &guess);

	if (0x1337c0dedeadbeef == (rn ^ guess)) {
		puts("Wow, what are the odds!");
		win();
	} else {
		puts("You had no chance anyway (1 in 18446744073709551616)");
	}
	return 0;
}
