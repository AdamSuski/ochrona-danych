#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TAJNY_PIN 1234

int main(int ac, char **av){
          int pin;
          if (av[1][0] == '-') {
                  printf("Atak zablokowany\n");
                  exit(1);
          } 
	  sscanf(av[1], "%u", &pin);
	  if (pin == TAJNY_PIN) {
                  printf("PIN poprawny\n");
          } else {
                  printf("PIN bledny\n");
          }
}

//2 ataki i 1 obrona
//zad 3 uruchomic shellcode.bin
