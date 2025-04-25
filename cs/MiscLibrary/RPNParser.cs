using System.Collections.Generic;

namespace MiscLibrary
{
    public static class RPNParser
    {
        /// <summary>
        /// Преобразует обычное математическое выр-е в обратную польскую запись
        /// </summary>
        /// <param name="initialString"> Начальное выражение </param>
        /// <returns> Обратная польская запись выражения </returns>
        public static string ToRPN(string initialString)
        {
            // В стеке будут содержаться операции из выражения
            Stack<char> operationsStack = new Stack<char>();

            // Результирующая строка
            string result = string.Empty;
            // Удаляем из входной строки лишние пробелы
            initialString = initialString.Replace(" ", "");

            foreach (var letter in initialString)
            {
                // Если текущий символ - число, добавляем его к результирующей строке
                //
                if (char.IsDigit(letter))
                {
                    result += letter;
                    continue;
                }

                // Если текущий символ - операция (+, -, *, /)
                //
                if (IsOperation(letter))
                {
                    // Если это не первая операция в выражении,
                    // то нам необходимо будет сравнить ее
                    // с последней операцией, хранящейся в стеке.
                    // Для этого сохраняем ее в переменной lastOperation
                    //
                    char lastOperation;
                    if (operationsStack.Count != 0)
                        lastOperation = operationsStack.Peek();

                    // Иначе (если это первая операция), кладем ее в стек,
                    // и переходим к следующему символу
                    else
                    {
                        operationsStack.Push(letter);
                        continue;
                    }

                    // Если приоритет текущей операции больше приоритета
                    // последней, хранящейся в стеке, то кладем ее в стек
                    //
                    if (GetOperationPriority(lastOperation) < GetOperationPriority(letter))
                    {
                        operationsStack.Push(letter);
                        continue;
                    }

                    // иначе, выталкиваем последнюю операцию,
                    // а текущую сохраняем в стек
                    else
                    {
                        result += operationsStack.Pop();
                        operationsStack.Push(letter);
                        continue;
                    }
                }

                // Если текущий символ - '(', кладем его в стек
                if (letter.Equals('('))
                {
                    operationsStack.Push(letter);
                    continue;
                }

                // Если текущий символ - ')', то выталкиваем из стека
                // все операции в результирующую строку, пока не встретим знак '('.
                // Его в строку не закидываем.
                if (letter.Equals(')'))
                {
                    while (operationsStack.Peek() != '(')
                    {
                        result += operationsStack.Pop();
                    }
                    operationsStack.Pop();
                }
            }

            // После проверки всей строки, выталкиваем из стека оставшиеся операции
            while (operationsStack.Count != 0)
            {
                result += operationsStack.Pop();
            }

            // Возвращаем результат
            return result;
        }

        /// <summary>
        /// Вычисляет результат выражения, записанного в обратной польской нотации
        /// </summary>
        /// <param name="rpnString"> Обратная польская запись выражения </param>
        /// <returns> Результат выражения </returns>
        public static int CalculateRPN(string rpnString)
        {
            // В стеке будут храниться цифры из ОПН
            Stack<int> numbersStack = new Stack<int>();



            foreach (var letter in rpnString)
            {
                // Если символ - цифра, помещаем его в стек,
                if (char.IsDigit(letter))
                    numbersStack.Push(int.Parse(letter.ToString()));

                // иначе (символ - операция), выполняем эту операцию
                // для двух последних значений, хранящихся в стеке.
                // Результат помещаем в стек
                else
                {
                    int op2 = numbersStack.Pop();
                    int op1 = numbersStack.Pop();
                    numbersStack.Push(ApplyOperation(letter, op1, op2));
                }
            }

            // Возвращаем результат
            return numbersStack.Pop();
        }

        /// <summary>
        /// Проверяет, является ли символ математической операцией
        /// </summary>
        /// <param name="c"> Символ для проверки</param>
        /// <returns> true, если символ - операция, иначе false</returns>
        private static bool IsOperation(char c)
        {
            if (c == '+' ||
                c == '-' ||
                c == '*' ||
                c == '/')
                return true;
            return false;
        }

        /// <summary>
        /// Определяет приоритет операции
        /// </summary>
        /// <param name="c"> Символ операции </param>
        /// <returns> Ее приоритет </returns>
        private static int GetOperationPriority(char c)
        {
            switch (c)
            {
                case '+': return 1;
                case '-': return 1;
                case '*': return 2;
                case '/': return 2;
                default: return 0;
            }
        }

        /// <summary>
        /// Выполняет матем. операцию над двумя числами
        /// </summary>
        /// <param name="operation"> Символ операции </param>
        /// <param name="op1"> Первый операнд </param>
        /// <param name="op2"> Второй операнд </param>
        /// <returns> Результат операции </returns>
        private static int ApplyOperation(char operation, int op1, int op2)
        {
            switch (operation)
            {
                case '+': return (op1 + op2);
                case '-': return (op1 - op2);
                case '*': return (op1 * op2);
                case '/': return (op1 / op2);
                default: return 0;
            }
        }
    }
}
