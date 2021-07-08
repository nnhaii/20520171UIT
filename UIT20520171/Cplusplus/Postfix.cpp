#include <iostream>
#include <stack>
#include <string>
#include <limits.h>
#include <cmath>

using namespace std;

float sNumber(char ch){
   int value;
   value = ch;
   return float(value-'0');
}
int isOperator(char ch){
    if(ch == '+'|| ch == '-'|| 
       ch == '*'|| ch == '/'|| 
       ch == '^')
      return 1;
    return -1;
}
int isOperand(char ch){
    if(ch >= '0' && ch <= '9') 
        return 1;
    return -1;
}
float operation(int a, int b, char op){
    if(op == '+') return b+a;
    if(op == '-') return b-a;
    if(op == '*') return b*a;
    if(op == '/') return b/a;
    if(op == '^') return pow(b,a);
    return INT_MIN;
}
float Eval(string hauto){
    int a, b;
    stack <float> stackk;
    for(string::iterator i = hauto.begin(); i != hauto.end(); i++){
       if(isOperator(*i) != -1){
         a = stackk.top(); stackk.pop();
    b = stackk.top(); stackk.pop();
         stackk.push(operation(a, b, *i));
       }
       else if(isOperand(*i) > 0){
           stackk.push(sNumber(*i));
       }
    }
    return stackk.top();
}
int main(){
    string post;
    getline(cin, post);
    cout<<Eval(post);
    return 0;
}