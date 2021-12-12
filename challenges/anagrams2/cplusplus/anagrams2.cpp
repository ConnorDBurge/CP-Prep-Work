#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isCharacterMatch(string string1, string string2)
{
    // get raw character list with no whitespace to compare against each other
    vector<char> string1chars;
    vector<char> string2chars;

    for (int i = 0; i < string1.length(); i++)
    {
        string1chars.push_back(string1[i]);
    }
    for (int i = 0; i < string2.length(); i++)
    {
        string1chars.push_back(string2[i]);
    }

    if (string1chars.size() == string2chars.size())
    {
        for (int i = 0; i < string1.length(); i++)
        {
            if (std::count(string2chars.begin(), string2chars.end(), string1chars[i]) == 0)
            {
                return false; // false when different char is found
            }
        }
        return true;
    }
    // returns if strings are not equal size
    return false;
}

void anagrams(string word, vector<string> listOfWords)
{
    for (int i = 0; i < listOfWords.size(); i++)
    {
        if (isCharacterMatch(word, listOfWords[i]))
        {
            printf("%s\n", listOfWords[i].c_str());
        }
    }
}

int main()
{
    vector<string> listOfWords;
    listOfWords.push_back("threads");
    listOfWords.push_back("trashed");
    listOfWords.push_back("hardest");
    listOfWords.push_back("hounds");

    anagrams("threads", listOfWords);
}