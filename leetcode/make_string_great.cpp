#include <string>
#include <stack>

using namespace std;

class Solution {
public:
  string makeGood(string s){
    stack<char> stackChar;
    for(int i=0; i<s.size(); i++){
      char c = s[i];
      if(stackChar.size()>0){
        char topChar = stackChar.top();
        if (abs(c - topChar)==32){
          stackChar.pop();
        }else{
          stackChar.push(c);
        }
      }else{
        stackChar.push(c);
      }
    }

    string ans = "";

    while(!stackChar.empty()){
      char c = stackChar.top();
      ans = c + ans;
      stackChar.pop();
    }

    return ans;
  }
};
