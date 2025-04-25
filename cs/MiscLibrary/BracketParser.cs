using MyCollectionsLibrary;

namespace MiscLibrary
{
    public static class BracketParser
    {
        public static bool Parse(string s)
        {
            MyStack<char> myCharStack = new MyStack<char>();
            foreach (char item in s)
            {
                if (item == '(' || item == '[' || item == '{')
                {
                    myCharStack.Push(item);
                }
                else
                {
                    if (myCharStack.Count <= 0) return false;
                    switch (myCharStack.Pop())
                    {
                        case '(':
                            if (!(item == ')'))
                            {
                                return false;
                            }
                            break;
                        case '[':
                            if (!(item == ']'))
                            {
                                return false;
                            }
                            break;
                        case '{':
                            if (!(item == '}'))
                            {
                                return false;
                            }
                            break;
                    }
                }
            }

            if (myCharStack.Count == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
