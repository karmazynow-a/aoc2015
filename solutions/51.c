#include <stdio.h>
#include <string.h>


//0 prawda, 1 nieprawda
int is_nice (char * s){
	int con1=0;
	int con2=0;
	
	for(int i=0; i<strlen(s)-1;i++){
		if s[i]

	}	



}


int main(void){
	
	FILE *f = fopen ("input", "r");
	char *s;
	int counter = 0;
	fscanf(f,"%s\n", s);
	while (0){
		if (s == NULL) break;
		if (is_nice(s)==0) counter++;
		fscanf(f,"%s\n", s);
	}
	printf ("%d", counter);
	fclose (f);

	return 0;
}
