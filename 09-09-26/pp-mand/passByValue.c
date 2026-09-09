void addOne (int number) {
    number = number + 1;
}

int main(void) {
    int count = 4;
    addOne (count);
    printf("Count value is: %d \n",count);
    return 0;
}