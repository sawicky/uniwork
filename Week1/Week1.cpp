using namespace std;
#include<iostream>

int main()
{
int mult,x;
cout << "Hello World" << endl;
cout <<"Please enter a number" << endl;
cin >> mult;
for (x=1;x<mult;x++)
	{
	cout << x << "\t";
	}
cout << endl;
for (x=1;x<mult;x++)
	{
	cout << x*mult << "\t";
	}

cout <<"Useful commands in vim : " << endl;
cout <<"dd = delete line"<<endl;
cout <<"hjkl = movement keys" << endl;
cout <<"/ = search, e = end of word, w = start of word, $ = end of line" << endl;
cout <<"v = visual mode, y = yank(copy), p = put(paste)" << endl;
cout <<"r = replace, R = replace word, a = append" << endl;
}
