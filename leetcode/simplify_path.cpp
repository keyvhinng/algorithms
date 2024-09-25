#include <stack>
#include <string>
#include <vector>

using namespace std;


class Solution {
public:
  string simplifyPath(string path){
    vector<string> parts;   
    size_t start = 0;
    size_t end   = path.find('/');
    string token;
    while(end != string::npos){
      token = path.substr(start, end-start);
      parts.push_back(token);
      start = end + 1;
      end = path.find('/',start);
    }
    parts.push_back(path.substr(start));
    stack<string> pathStack;
    for(int i=0; i<parts.size(); i++){
      token = parts[i];
      if (token == ""){
      }else if(token == "."){
      }else if(token == ".."){
        if(!pathStack.empty()){
          pathStack.pop();
        }
      } else {
        pathStack.push(token);
      }
    }
    stack<string> auxStack;
    while(!pathStack.empty()){
      auxStack.push(pathStack.top());
      pathStack.pop();
    }
    string ans = "";
    if (auxStack.size() == 0 ){
      ans = "/";
    }else{
      while(!auxStack.empty()){
        string s = auxStack.top();
        ans = ans + "/" + s;
        auxStack.pop();
      }
    }

    return ans;
  }
};
