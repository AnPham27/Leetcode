/*
 * Submitted on October 25, 2022
 * Question: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 */
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        
        //Use stack to push LEFT brackets and pop RIGHT brackets
        
        //Stack stack1 = new Stack();
        
        Stack<Character> stack = new Stack<Character>();
        
        char index = ' ';
       
        
        for (int i = 0; i< s.length(); i++) {
            
            
            //if it's empty and it is a closing bracket... not valid
            if (stack.empty() && (s.charAt(i) == ')' || s.charAt(i) == ']' || s.charAt(i) == '}')) {
                return false;
            }
            

            //if it's a closing bracket EVER ... add into stack
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                
                stack.push(s.charAt(i));
                
            }
            
            //if they match, pop! 
            else if ((s.charAt(i) == ')' && stack.peek() == '(') || (s.charAt(i) == ']' && stack.peek() == '[') || (s.charAt(i) == '}' && stack.peek() == '{')) {
                stack.pop();
            } 
            
            //if they don't match and is not an opening bracket, it's not valid
            else {
                return false;
            }
        
                
            
            
        }
        
        //if it's full of opening brackets with no closing brackets, it's not empty so ... not valid
        return stack.empty();