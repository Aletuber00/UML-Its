
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
   
    //TRACCIA

// chiedere all utente N numeri al max 100 numeri interi compresi tra 0 e 2026
// visualizzare tutti i numeri almeno duplicati
// per ogni numero almeno duplicato visualizzare su msg del tipo
// "il numero 4 è presente 3 volte nelle posizioni 5 8 e 10"
// un ulteriore array alla fine 
    
     // RISORSE DA DEFINIRE
 // N                conterrà QUANTI
 // numeri           array di N elementi che contiene i numeri interi (min 2 max 100)
 // conta            quanti duplicati ci sono
 // duplicati     array (max 100) che contiene True se quella posizione contiene un duplicato 
 //                                     False se quella posizione NON contiene un duplicato
 // posizioni        array (max 100) che contiene le posizioni dei valori duplicati

    //STEP DA SEGUIRE

//1. chiedere in input QUANTI numeri vuole inserire (da 0 a 2026)
//2. inserire i QUANTI numeri nell array
//3. popolare l array NUMERI (da 0 a 2026)
//4. per ogni iterazione dobbiamo
    //a. verificare se ci sono duplicati
    //    se ci sono duplicati bisogna contare i duplicati nella variabile CONTA
    //    memorizzare le posizioni in un nuovo array POSIZIONI
    //    contrassegnare quella posizione con TRUE
//5. Per ogni duplicato stampare 
    
    int N = 0;
    const int DIMENSIONE_MAX = 100;
    const int DIMENSIONE_MIN = 2;
    int numeri[DIMENSIONE_MAX];
    for(int i=0;i<DIMENSIONE_MAX;i++){
             numeri[i] = 0;
            }
    int conta = 0;

    bool duplicati[DIMENSIONE_MAX];
    for(int i=0;i<DIMENSIONE_MAX;i++){
             duplicati[i] = false;
            }
    
    int posizioni[DIMENSIONE_MAX];
     for(int i=0;i<DIMENSIONE_MAX;i++){
             posizioni[i] = 0;
            }  


     do { 
            printf("Quanti numeri vuoi inserire? (massimo 100)");
            scanf("%d",&N);       
        } while (N < DIMENSIONE_MIN || N > DIMENSIONE_MAX);
         

        for (int i = 0;i < N;i++) {
            do
            {
                printf("Inserisci il %d* numero",i+1);
                scanf("%d", &numeri[i]);  
            } while (numeri[i]<0 || numeri[i]>2026);
              
            
        }
}