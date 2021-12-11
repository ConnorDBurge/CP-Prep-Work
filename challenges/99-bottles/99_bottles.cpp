#include <iostream>

void bottleSong(int num)
{
    for (int i = num; i > 0; i--)
    {
        std::string plural = "s ";
        if (i < 1)
        {
            plural = " ";
        }

        printf("%d bottle%sof beer on the wall, %d bottle%sof beer.\n", i, plural.c_str(), i, plural.c_str());

        if (i > 1)
        {
            printf("Take one down and pass it around, %d bottle%sof beer on the wall.\n", i - 1, plural.c_str());
        }
    }
    printf("Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, %d bottles of beer on the wall.", num);
}

int main()
{
    bottleSong(5);
}