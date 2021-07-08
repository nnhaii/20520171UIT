#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string post;
    getline(cin, post);
	//post = "((237988009*(6-1))/2)*4";
    for(int i = 0; i < post.size(); i++){
        if (int(post[i]) == 40) {
            cout << post[i] << " open_parenthesis\n";
            continue;
        }
        if (int(post[i]) == 41) {
            cout << post[i] << " close_parenthesis\n";
            continue;
        }
        if (int(post[i]) == 42 || int(post[i]) == 43 
            || int(post[i]) == 45 || int(post[i]) == 47){
            cout << post[i] <<" operator\n";
            continue;
        }
        int s = 0;
        int j = i;
        while (int(post[j]) >= 48 && int(post[j]) <= 57){
            s=s*10 + int(post[j]) - 48;
            j++;
        }
        i = j;
        cout << s << " operand\n";
    }
    return 0; 
}
 