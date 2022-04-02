#include <stdio.h>
#include <string.h>

#define TAM 20

struct{
	int edad;
	char nombre[TAM];
	char apellidos[TAM*2];
}Persona;
void caminar(int pasos);
void hablar(char* palabras);

struct{
	Persona persona;
	int id;
	int numCuenta;
	int saldo;
}Cliente;
void retirar(float cantidad);
void depositar(float cantidad);

struct{
	char nombre[TAM];
	int id;
	Cliente cliente;
}Banco;
void abrir();
void cerrar();

int main(){
	Persona p1;
	Cliente c1;
	Banco hsbc;
	return 0;
}
/*IsainJimenezMartinez*/