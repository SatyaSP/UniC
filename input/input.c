// void f(int a, int result[]) {
// 	count = a ;            /* count not defined? */
// }

// int count;
// int result[50];

// int main ( void ) {
//     int i;
//     void a;
//     i = result;                /* type mismatch? */
//     count = f(i, result);      /* function returns void */
// 	f(i + a, i * result);      /* what are the types of the arguments? */
//     if (a == f(i, result)) {   /* void types match in comparison? */
//         continue;              /* not inside while although properly nested */
//     }
//     else{} 
// }

/*
int count;
int result[50];


int f(int a, int result[]) {
    count = count + 1;
    if(result[a - 1]){
        return result[a - 1];
    } else {
        if (a == 1) {
            result[a - 1] = 1;
            return 1;
        } else if (a == 2){
            result[a - 1] = 1;
            return 1;
        } else {
            result[a - 1] = f(a - 2, result) + f(a - 1, result);
            return result[a - 1];
        }
    }
}

*/

/*
void main(void) {
    int i;
    i = 0;
    while (i < 50) {
        result[i] = 0;
        i = i + 1;
    }
    count = 0;
    output(f(40, result));
    output(count);
}
*/


void main(void){
    int i ;
    i = 7;
    switch(i){
        case 3:
            output(7);
            break;
        default:
            output(0);
            break;
    }    
}