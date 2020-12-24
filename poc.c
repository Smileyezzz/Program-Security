#include <stdio.h>
#include <stdlib.h>
#define int64 long long int
    
int payload[70] = {0};
int flag[70] = {0};

int init_arr[] = {85, 51, 70, 68, 107, 46, 17, 105, 109, 61,
                  67, 112, 106, 29, 106, 68, 46, 94, 105, 51,
                  26, 109, 26, 22, 44, 123, 92, 111, 35, 64, 103,
                  55, 57, 101, 33, 100, 47, 42, 116, 73, 119, 98,
                  42, 125, 38, 3, 38, 50, 65, 99, 77, 16, 34, 36,
                  15, 42, 55, 10, 92, 56, 44, 49, 65, 61, 118, 82, 88, 27, 91, 31};



void check_multi(int jmp, int offset, int check_1, int check_2){
    for (int i = 48; i < 91; ++i){
        if (check_1 == (135 *i))
            payload[offset] = i;
    }
    jmp--;
    if (jmp){
        for (int i = 48; i < 91; ++i){
            if (check_2 == (135 *i))
                payload[offset+1] = i;
        }
    }
}

void check_minus(int jmp, int offset, int check_1, int check_2){
    for (int i = 48; i < 91; ++i){
        int var = -88035316;
        for (int j = 0; j < i; ++j){
            if (j & 1)
                var -= 120;
            else
                var -= 30600;
        }
        if (check_1 == var)
            payload[offset] = i;
    }
    jmp--;
    if (jmp){
        for (int i = 48; i < 91; ++i){
            int var = -88035316;
            for (int j = 0; j < i; ++j){
                if (j & 1)
                    var -= 120;
                else
                    var -= 30600;
            }
            if (check_2 == var)
                payload[offset+1] = i;
        }
    }
}
void check_xor(int jmp, int offset, int check_1, int check_2){
    int magic_num = 1383424633;
    for (int i = 48; i < 91; ++i){
        if (check_1 == (i ^ magic_num))
            payload[offset] = i;
    }
    jmp--;
    if (jmp){
        for (int i = 48; i < 91; ++i){
            if (check_2 == (i ^ magic_num))
                payload[offset+1] = i;
        }
    }

}
void check_add(int jmp, int offset, int check_1, int check_2){
    for (int i = 48; i < 91; ++i){
        int var = 0;
        for (int j = 0; j < i; ++j){
            if (j & 1)
                var += 2;
            else
                var += 11;
        }
        if (check_1 == var)
            payload[offset] = i;
    }

    jmp--;
    if (jmp){
        for (int i = 48; i < 91; ++i){
                int var = 0;
                for (int j = 0; j < i; ++j){
                    if (j & 1)
                        var += 2;
                    else
                        var += 11;
                }
                if (check_2 == var)
                    payload[offset+1] = i;
        }
    }
}

void check_fibo(int jmp, int offset, int check_1, int check_2){
    for (int i = 48; i < 91; ++i){
        int var_0 = 0;
        int var_1 = 1;
        int var_2 = 0;

        for (int j = 0; j < i; ++j){
            var_2 = var_0 + var_1;
            var_0 = var_1;
            var_1 = var_2;
        }
        if (var_2 == check_1)
            payload[offset] = i;
    }
    jmp--;
    
    if (jmp){
        for (int i = 48; i < 91; ++i){
            int var_0 = 0;
            int var_1 = 1;
            int var_2 = 0;

            for (int j = 0; j < i; ++j){
                var_2 = var_0 + var_1;
                var_0 = var_1;
                var_1 = var_2;
            }
            if (var_2 == check_2)
                payload[offset+1] = i;
        }
    }

}

void do_xor(int *array_1, int *array_2){
    for (int i = 0; i < 70; ++i)
        array_1[i] = array_1[i] ^ array_2[i];
}

int main(){
	// len of init_arr is 70
    int idx = 0;
    int k = 0;
    int count = 0;
    while(count < 1000){
        if (idx > 69){
            count ++;
            do_xor(init_arr, payload);
            idx = 0;
        }

        int func_call = magic_array[k] + magic_array[k+4];
        switch(func_call){
            case 4198334:   // 0x400fbe
                check_multi(magic_array[k+6], magic_array[k+5], magic_array[k+7], magic_array[k+8]);
            case 4198445:   // 0x40102d
                check_add(magic_array[k+6], magic_array[k+5], magic_array[k+7], magic_array[k+8]);
            case 4198712:   // 0x401138
                check_minus(magic_array[k+6], magic_array[k+5], magic_array[k+7], magic_array[k+8]);
            case 4198600:   // 0x4010c8
                check_xor(magic_array[k+6], magic_array[k+5], magic_array[k+7], magic_array[k+8]);
            case 4198870:   // 0x4011d6
                check_fibo(magic_array[k+6], magic_array[k+5], magic_array[k+7], magic_array[k+8]);
        }
        idx += magic_array[k+6];
        k += 10;
        
    }
    
    printf("\n");
    for(int i = 0; i < 70; ++i){
        printf("%c",init_arr[i]);
    }
    printf("\n");
    
    return 0;
}
